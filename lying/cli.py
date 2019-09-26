"""The command line interface"""
import json
from argparse import ArgumentParser
from logging import basicConfig
from lying import __version__
from lying.terminal import Terminal
from lying.utils.dispatch import Dispatchers


def create_parser():
    """Create the parser"""
    parser = ArgumentParser(
        description='Run a fake terminal',
        epilog='lying {} by AxJu'.format(__version__),
    )
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='verbosity (-v, -vv, etc)'
    )
    subparsers = parser.add_subparsers(help='commands', dest='command')

    parser_run = subparsers.add_parser('run')
    parser_run.add_argument('file', help='the filename')
    parser_run.add_argument('-c', '--clean', action='store_false', help='Disable clean the scrren befot start')
    parser_run.add_argument('-a', '--auto_exit', action='store_false', help='Disable auto exit after finished')
    parser_run.add_argument('--prompt', help='Set terminal promplt')
    parser_run.add_argument('--wait', type=int, help='Set wait in ms')

    parser_setup = subparsers.add_parser('setup')
    parser_setup.add_argument('file', help='the filename')

    return parser


def get_settings(args):
    """Get settings from args"""
    settings = {}
    for key in ['prompt', 'wait']:
        value = getattr(args, key, False)
        if value:
            settings[key] = value
    return settings


def setup_logger(verbose):
    """Setup logger"""
    level = (3 - verbose) * 10 if verbose in range(3) else 50
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    basicConfig(level=level, format=log_format)


def run(args):
    """Run the terminal"""
    terminal = Terminal()
    terminal.load(args.file)
    terminal.settings.load(**get_settings(args))
    terminal.run(args.clean, args.auto_exit)


def setup(args):
    """Setup some instructions and settings"""
    instructions = []
    settings = {}

    settings['prompt'] = input('Set prompt [>>> ] ') or '>>> '

    while True:
        dispatchers = Dispatchers()
        for item in dispatchers:
            print('{:>8} {} {}'.format(item[0], item[1].__doc__, item[1].kwargs))

        name = input('Select on [q=exit] : ') or 'q'
        if name in ['quit', 'q', 'x']:
            break

        print('You select "{}":'.format(name))
        kwargs = {}
        for attr, kind in dispatchers[name].kwargs.items():
            kwargs[attr] = kind(input('Set value for {}: '.format(attr)))
        instructions.append((name, kwargs))

    if instructions or settings:
        with open(args.file, 'w') as file:
            json.dump({'settings': settings, 'instructions': instructions}, file, indent=4)


def main(args=None):
    """entry point for the main cli"""
    parser = create_parser()
    args = parser.parse_args(args)
    if args.command == 'run':
        run(args)
    elif args.command == 'setup':
        setup(args)


if __name__ == '__main__':
    main()

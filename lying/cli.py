"""The command line interface"""
import json
from argparse import ArgumentParser
from logging import getLogger, FileHandler, StreamHandler, Formatter
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
    parser.add_argument('--log', help='Set a logfile')
    subparsers = parser.add_subparsers(help='commands', dest='command')

    parser_run = subparsers.add_parser('run')
    parser_run.add_argument('file', help='the filename')
    parser_run.add_argument('-c', '--clean', action='store_false', help='Disable clean the scrren befot start')
    parser_run.add_argument('-a', '--auto_exit', action='store_false', help='Disable auto exit after finished')
    parser_run.add_argument('-f', '--fast', action='store_true', help='Run without a time delay')
    parser_run.add_argument('--prompt', help='Set terminal promplt')
    parser_run.add_argument('--delay', type=int, default=0, help='Start with a delay of n sec.')

    parser_setup = subparsers.add_parser('setup')
    parser_setup.add_argument('file', help='the filename')

    return parser


def get_settings(args):
    """Get settings from args"""
    settings = {}
    for key in ['prompt', 'fast']:
        value = getattr(args, key, False)
        if value:
            settings[key] = value
    return settings


def setup_logger(verbose, filename=None):
    """Setup logger"""
    level = (3 - verbose) * 10 if verbose in range(3) else 50
    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = getLogger()
    logger.setLevel(level)
    handler = FileHandler(filename) if filename else StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def run(args):
    """Run the terminal"""
    terminal = Terminal()
    terminal.load(args.file)
    terminal.settings.load(**get_settings(args))
    terminal.run(args.clean, args.auto_exit, args.delay)


def setup(args):
    """Setup some instructions and settings"""
    instructions = []
    settings = {}

    settings['prompt'] = input('Set prompt [>>> ] ') or '>>> '

    dispatchers = Dispatchers()
    width = max([len(item[0]) for item in dispatchers])
    while True:
        for item in dispatchers:
            print('{:>{width}} : {}'.format(item[0], item[1].__doc__, width=width))

        name = input('Select on [q=exit+save]: ') or 'q'
        if name in ['quit', 'q', 'x']:
            break

        print('You select "{}":'.format(name))
        kwargs = {}
        for attr, kind in dispatchers[name].__kwargs__.items():
            if isinstance(kind, (tuple, list)):
                kwargs[attr] = kind[0](input('Set value for {} [{}]: '.format(attr, kind[1])) or kind[1])
            elif isinstance(kind, type):
                kwargs[attr] = kind(input('Set value for {} [{}]: '.format(attr, kind())) or kind())
        instructions.append((name, kwargs))

    if instructions or settings:
        with open(args.file, 'w') as file:
            json.dump({'settings': settings, 'instructions': instructions}, file, indent=4)


def main(args=None):
    """entry point for the main cli"""
    parser = create_parser()
    args = parser.parse_args(args)
    setup_logger(args.verbose, args.log)
    if args.command == 'run':
        run(args)
    elif args.command == 'setup':
        setup(args)


if __name__ == '__main__':
    main()

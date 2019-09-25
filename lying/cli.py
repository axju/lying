"""The command line interface"""
import os
from argparse import ArgumentParser
from logging import basicConfig
from lying import __version__
from lying.terminal import Terminal


def main(args=None):
    """entry point for the main cli"""
    parser = ArgumentParser(
        description='Run a fake terminal',
        epilog='lying {} by AxJu'.format(__version__),
    )
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='verbosity (-v, -vv, etc)'
    )
    subparsers = parser.add_subparsers(help='sources', dest='source')

    parser_file = subparsers.add_parser('file')
    parser_file.add_argument('filename', help='the filename')

    parser_bash = subparsers.add_parser('bash')
    parser_bash.add_argument('-c', '--count', type=int, default=5, help='the n-th last lines')

    args = parser.parse_args(args)

    level = (3 - args.verbose) * 10 if args.verbose in range(3) else 50
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    basicConfig(level=level, format=log_format)

    if args.source == 'bash':
        filename = os.path.join(os.path.expanduser('~'), '.bash_history')
        if not os.path.exists(filename):
            return 0
        with open(filename) as file:
            buffer = file.readlines()

        data = list(map(str.strip, buffer[-args.count:]))
        terminal = Terminal()
        terminal.load(data=data)
        terminal.run()




if __name__ == '__main__':
    main()

#!/usr/bin/env python3

# TODO: Make commands callable

import argparse
from scripts.reminder import scheduled, instant, check, upcoming, stop


def main() -> None:
    scheduled()
    parser = create_parser()


def create_parser() -> argparse.ArgumentParser:
    # TODO: Refactor! Maybe make this into a different helper function in a separate file?
    parser = argparse.ArgumentParser(prog='Sends reminder text to designated phone number')
    parser.add_argument('-r', '--remind',
                        help='sends immediate reminder text',
                        action='store_true')
    parser.add_argument('-c', '--check',
                        help='prints out when last message was sent',
                        action='store_true')
    parser.add_argument('-n', '--next',
                        help='time until the next text message is sent',
                        action='store_true')
    parser.add_argument('-s', '--stop',
                        help='stops program from sending future texts',
                        action='store_true')

    args = parser.parse_args()

    if args.remind:
        instant()
    elif args.check:
        check()
    elif args.next:
        upcoming()
    elif args.stop:
        stop()

    return parser


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import argparse
from scripts.reminder import *


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if args.remind:
        instant()
    elif args.check:
        check()
    elif args.next:
        upcoming()
    elif args.enable:
        enable()
    elif args.disable:
        disable()
    else:
        scheduled()


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='Sends reminder text to designated phone number')
    parser.add_argument('-r', '--remind',
                        help='sends immediate reminder text',
                        action='store_true')
    parser.add_argument('-c', '--check',
                        help='prints out when last text message was sent',
                        action='store_true')
    parser.add_argument('-n', '--next',
                        help='time the next text message is sent',
                        action='store_true')
    parser.add_argument('-e', '--enable',
                        help='starts program to send regularly scheduled texts',
                        action='store_true')
    parser.add_argument('-d', '--disable',
                        help='stops program schedule from sending future texts',
                        action='store_true')
    return parser


if __name__ == '__main__':
    main()

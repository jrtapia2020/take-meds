#!/usr/bin/env python3

# TODO: Add argument parser and command line options
# TODO: Make reminder callable along with other future commands

"""
List of future commands in run.py for project:
- check: checks to see if program ran within the last 24 hours
- next: checks to see how long until the next message will be sent
"""

from reminder import reminder


def main() -> None:
    reminder()


if __name__ == '__main__':
    main()

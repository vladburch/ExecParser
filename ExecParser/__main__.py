#!/usr/bin/env python3
#
# Author:
#  Vladislav Burtsev (https://github.com/r33-L1)
#

import os
import logging


def main():
    import argparse
    import glob

    from ExecParser import logger

    parser = argparse.ArgumentParser(description='Executable files analyzing and modification')
    parser.add_argument('-v', '--verbose', action="count", default=0,
                        help='Set verbosity level')
    parser.add_argument('--version', action="store_true",
                        help='Print current version of ExecParser')

    # PARSING ARGUMENTS
    args = parser.parse_args()

    # VERBOSITY
    if args.verbose == 0:
        logging.basicConfig(level=logging.INFO)
        logger.setLevel(logging.INFO)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:
        level = 5 - args.verbose
        logging.basicConfig(level=level)
        logger.setLevel(1)

    # VERSION
    if args.version:
        from ExecParser._version import __version__
        print(__version__)
        from ExecParser._version import __banner__
        print(__banner__)
        from ExecParser._version import __logo__
        print(__logo__)


if __name__ == '__main__':
    main()
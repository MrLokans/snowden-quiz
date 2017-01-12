from __future__ import print_function
import os
import logging
import argparse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class SnowdenSolver(object):

    def solve(self, encrypted_text):
        """
        Decrypts encoded text
        """
        return ""


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Path to the input file')
    return parser.parse_args()


def main():
    args = parse_args()

    exists = os.path.exists(args.input_file)
    if not exists or not os.path.isfile(args.input_file):
        logger.warn("File {name} does not exist or is a directory"
                    .format(name=args.input_file))
        return

    data = ""
    logger.debug("Reading input file {name} contents"
                 .format(name=args.input_file))
    with open(args.input_file, 'r') as f:
        data = f.read()
    solver = SnowdenSolver()
    result = solver.solve(data)
    print(result)


if __name__ == '__main__':
    main()

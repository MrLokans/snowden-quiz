from __future__ import print_function
import os
import itertools
import logging
import argparse


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


class SnowdenSolver(object):

    @staticmethod
    def _is_list_encrypted(char_lists):
        for el in char_lists:
            if len(el) > 1:
                return True
        return False

    @staticmethod
    def _remove_duplicates(char_lists):
        new_list = []
        for indx, el in enumerate(char_lists):
            if len(el) > 1:
                if len(el) % 2 == 0:
                    continue
                else:
                    new_list.append(el[0])
            else:
                new_list.extend(el)
        return new_list

    def solve(self, encrypted_text):
        """
        Decrypts encoded text

        Worst-case scenario is when our impurt string
        is a palindrome without repeated symbols
        """
        groupped = [list(g) for _, g in itertools.groupby(encrypted_text)]
        while self._is_list_encrypted(groupped):
            groupped = self._remove_duplicates(groupped)
            groupped = [list(g) for _, g in itertools.groupby(groupped)]
        return "".join(itertools.chain(*groupped))


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

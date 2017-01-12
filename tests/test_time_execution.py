import random
import string
import time

from six.moves import range
import pytest

from snowden import SnowdenSolver

MAX_LENGTH = 10000000
INSERTED_LENGTH = 2
NUMBER_OF_INSERTED_CHAR_PAIRS = 500

MAX_TEST_DURATION_SECONDS = 1


def generate_letter_pairs(count):
    """
    Yields the specified amount
    of lowercase ascii character pairs

    :param count: number of pairs to yield
    :type count: int
    """
    for _ in range(count):
        yield random.choice(string.ascii_lowercase) * 2


@pytest.fixture()
def max_len_string():
    length_wo_pairs = MAX_LENGTH - NUMBER_OF_INSERTED_CHAR_PAIRS * INSERTED_LENGTH

    # Fits into the memory
    s = [random.choice(string.ascii_lowercase)
         for _ in range(length_wo_pairs)]
    for pair in generate_letter_pairs(NUMBER_OF_INSERTED_CHAR_PAIRS):
        s.insert(random.randint(0, len(s) - 1), pair)
    return "".join(s)


def test_long_string_is_processed_fast(max_len_string):
    solver = SnowdenSolver()
    start_time = time.time()
    solver.solve(max_len_string)
    stop_time = time.time()

    assert stop_time - start_time < MAX_TEST_DURATION_SECONDS

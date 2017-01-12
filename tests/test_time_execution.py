import random
import string
import time
import itertools

from six.moves import range
import pytest

from snowden import SnowdenSolver

MAX_LENGTH = 1000000
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


@pytest.fixture()
def worst_case_string():
    # Worst case scenario is palindrome of non-consequentially
    # repeated characters
    half_size = MAX_LENGTH // 2
    s = []
    cycled = itertools.cycle(string.ascii_lowercase)
    i = 0
    while i < half_size:
        s.append(next(cycled))
        i += 1
    half_str = "".join(s)
    reversed_str = half_str[::-1]

    return half_str + reversed_str


def test_long_string_is_processed_fast(max_len_string):
    solver = SnowdenSolver()
    start_time = time.time()
    solver.solve(max_len_string)
    stop_time = time.time()

    test_duration = stop_time - start_time
    assert test_duration < MAX_TEST_DURATION_SECONDS


def test_worst_case_scenario_is_processed_fast(worst_case_string):
    solver = SnowdenSolver()
    start_time = time.time()
    solver.solve(worst_case_string)
    stop_time = time.time()

    test_duration = stop_time - start_time
    print(test_duration)
    assert test_duration < MAX_TEST_DURATION_SECONDS

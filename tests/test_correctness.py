import pytest

from snowden import SnowdenSolver


def test_processing_empty_string_returns_empty_string():
    solver = SnowdenSolver()
    result = solver.solve("")
    assert result == ""


def test_provided_example_is_solved_correctly():
    solver = SnowdenSolver()
    result = solver.solve("wwsndaadowffdennn")
    assert result == "snowden"


@pytest.mark.parametrize("test_input,expected_result", [
    ("a", "a"),
    ("nn", ""),
    ("anan", "anan"),
    ("nannan", ""),
])
def test_simple_inputs(test_input, expected_result):
    solver = SnowdenSolver()
    assert solver.solve(test_input) == expected_result

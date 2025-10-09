import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the function returns the longest of multiple streaks."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3

def test_with_negatives_and_zeros():
    """Test that zeros and negative numbers correctly break streaks."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    """Test a case with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_interspersed_positives():
    """Test a list where positive numbers are separated by non-positives."""
    assert longest_positive_streak([1, 0, 2, 0, 3]) == 1

def test_long_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 4, 5, 6, 7]) == 4

def test_from_example_one():
    """Test from the example: [2, 3, -1, 5, 6, 7, 0, 4] == 3"""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_from_example_two():
    """Test from the example: [] == 0"""
    assert longest_positive_streak([]) == 0

def test_from_example_three():
    """Test from the example: [1, 1, 1] == 3"""
    assert longest_positive_streak([1, 1, 1]) == 3
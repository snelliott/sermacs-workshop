"""
Unit and regression test for the sermacs_workshop package.
"""

# Import package, test suite, and other packages as needed
import sermacs_workshop as su
import pytest
import sys


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


def test_mean_int(num_list_3):
    """Sample test, will always pass so long as import statement worked"""
    mean = su.mean(num_list_3)
    assert mean == 3.0


@pytest.mark.parametrize("num_list, expected_mean", [([1, 2, 3, 4, 5], 3.0),
                                                     ([0, 2, 4, 6], 3),
                                                     ([1, 2, 3, 4], 2.5)])
def test_mean_float(num_list, expected_mean):
    assert su.mean(num_list) == expected_mean


def test_type_error():
    nums = 1
    with pytest.raises(TypeError):
        nums = su.mean(nums)


def test_nonintfloat():
    nums = ['1', '2', 'three']
    with pytest.raises(TypeError):
        nums = su.mean(nums)


@pytest.mark.parametrize('x', [1, 0])
@pytest.mark.parametrize('y', [2, 3])
def test_combine(x, y):
    assert abs(x + y) < 10

from main import Solution
def set_equals(a, b):
    """Helper function to compare lists of triplets without worrying about order"""
    return set(tuple(sorted(x)) for x in a) == set(tuple(sorted(y)) for y in b)


# Basic and edge test cases
def test_empty_input():
    s = Solution()
    assert s.threeSum([]) == []


def test_not_enough_numbers():
    s = Solution()
    assert s.threeSum([1, 2]) == []


def test_no_triplets():
    s = Solution()
    assert s.threeSum([1, 2, 3]) == []


def test_simple_triplets():
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert set_equals(s.threeSum(nums), expected)


def test_all_zeroes():
    s = Solution()
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]


def test_multiple_duplicates():
    s = Solution()
    nums = [-2, 0, 0, 2, 2]
    expected = [[-2, 0, 2]]
    assert set_equals(s.threeSum(nums), expected)


def test_large_input():
    s = Solution()
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 4, 4, 6, 6]
    expected = [
        [-4, -2, 6],
        [-4, 0, 4],
        [-4, 1, 3],
        [-4, 2, 2],
        [-2, -2, 4],
        [-2, 0, 2]
    ]
    assert set_equals(s.threeSum(nums), expected)

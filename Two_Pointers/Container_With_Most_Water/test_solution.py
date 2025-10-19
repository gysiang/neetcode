from main import Solution

def test_max_area_basic():
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_max_area_increasing_heights():
    s = Solution()
    assert s.maxArea([1,2,3,4,5]) == 6

def test_max_area_decreasing_heights():
    s = Solution()
    assert s.maxArea([5,4,3,2,1]) == 6

def test_max_area_equal_heights():
    s = Solution()
    assert s.maxArea([5,5,5,5]) == 15

def test_max_area_single_element():
    s = Solution()
    assert s.maxArea([10]) == 0

def test_max_area_empty_list():
    s = Solution()
    assert s.maxArea([]) == 0

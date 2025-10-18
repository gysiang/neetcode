from  main import Solution

def test_koko_basic():
    s = Solution()
    assert s.minEatingSpeed([3,6,7,11], 8) == 4

def test_koko_limited_time():
    s = Solution()
    assert s.minEatingSpeed([30,11,23,4,20], 6) == 23

def test_koko_single_pile():
    s = Solution()
    assert s.minEatingSpeed([1], 1) == 1

def test_koko_skewed_piles():
    s = Solution()
    assert s.minEatingSpeed([100,1,1,1], 4) == 100

def test_koko_large_dataset():
    s = Solution()
    assert s.minEatingSpeed([8]*1000000, 1000000) == 8

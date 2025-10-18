from main import Solution

def test_max_profit_basic():
    s = Solution()
    assert s.maxProfit([10, 1, 5, 6, 7, 1]) == 6

def test_max_profit_no_transactions():
    s = Solution()
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0

def test_max_profit_empty_list():
    s = Solution()
    assert s.maxProfit([]) == 0

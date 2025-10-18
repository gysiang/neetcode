from main import Solution, ListNode

# Helper function to create a linked list from a Python list
def list_to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to convert back into a list for comparison
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_reverse_list_basic():
    s = Solution()
    head = list_to_linked_list([1, 2, 3, 4, 5])
    reversed_head = s.reverseList(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_list_empty():
    s = Solution()
    head = list_to_linked_list([])
    reversed_head = s.reverseList(head)
    assert linked_list_to_list(reversed_head) == []

def test_reverse_list_single_element():
    s = Solution()
    head = list_to_linked_list([42])
    reversed_head = s.reverseList(head)
    assert linked_list_to_list(reversed_head) == [42]

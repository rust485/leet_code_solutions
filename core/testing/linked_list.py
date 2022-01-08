
from typing import Any, List, Optional
from core.model.listnode import ListNode


def assert_ll_equals_list(h: ListNode | None, expected: List[int]):
    actual = linked_list_to_array(h)
    assert actual == expected


def build_linked_list(arr: List[Any]) -> Optional[ListNode]:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])

    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head


def linked_list_to_array(head: Optional[ListNode]) -> List[Any]:
    if not head:
        return []

    result = []

    cur = head
    while cur:
        result += [cur.val]
        cur = cur.next

    return result


def print_linked_list(head: Optional[ListNode]) -> None:
    arr = linked_list_to_array(head)

    print(arr)

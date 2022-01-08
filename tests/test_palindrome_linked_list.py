from core.testing.linked_list import build_linked_list
from src.palindrome_linked_list.solution import Solution


def is_ll_palindrome(l: list[str]) -> bool:
    return Solution().isPalindrome(build_linked_list(l))


class TestPalindromeLinkedList:

    def test_is_true_if_empty(self):
        assert is_ll_palindrome([])

    def test_is_true_if_len_1(self):
        assert is_ll_palindrome(['a'])

    def test_is_true_for_even_list_with_palindrome(self):
        assert is_ll_palindrome(['a', 'b', 'b', 'a'])

    def test_is_true_for_odd_list_with_palindrome(self):
        assert is_ll_palindrome(['a', 'b', 'a'])

    def test_is_false_if_palindrome_except_first_and_last_characters(self):
        assert not is_ll_palindrome(['a', 'b', 'c', 'd', 'd', 'c', 'b', 'e'])

    def test_is_true_with_repeats(self):
        assert is_ll_palindrome(['a', 'a', 'a', 'a'])

    def test_is_false_no_repeats(self):
        assert not is_ll_palindrome(['a', 'b', 'c', 'd', 'e'])

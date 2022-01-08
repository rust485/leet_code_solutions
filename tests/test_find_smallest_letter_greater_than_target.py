from typing import List
from src.find_smallest_letter_greater_than_target.solution import Solution


def next_greatest_letter(l: List[str], c: str) -> str:
    return Solution().nextGreatestLetter(l, c)


class TestFindSmallestLetterGreatherThanTarget:
    def test_target_in_list(self):
        assert next_greatest_letter(['a', 'b', 'd'], 'b') == 'd'

    def test_target_not_in_list(self):
        assert next_greatest_letter(['a', 'b', 'd'], 'c') == 'd'

    def test_target_last_element_in_list(self):
        assert next_greatest_letter(['a', 'b', 'c', 'd'], 'd') == 'a'

    def test_target_not_in_list_and_comes_after_last_element(self):
        assert next_greatest_letter(['a', 'b', 'c', 'd'], 'e') == 'a'

    def test_target_comes_before_first_element_in_list(self):
        assert next_greatest_letter(['b', 'c', 'd'], 'a') == 'b'

    def test_target_only_element_in_list(self):
        assert next_greatest_letter(['a'], 'a') == 'a'

    def test_list_len_1_and_target_not_in_list(self):
        assert next_greatest_letter(['a'], 'b') == 'a'

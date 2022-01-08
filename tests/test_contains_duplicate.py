from src.contains_duplicate.solution import Solution


class TestContainsDuplicate:
    def test_empty_list(self):
        assert not Solution().containsDuplicate([])

    def test_list_with_no_duplicates(self):
        assert not Solution().containsDuplicate([10, 5, 7, 8, 22])

    def test_list_with_duplicates_at_front(self):
        assert Solution().containsDuplicate([10, 5, 4, 10, 3])

    def test_list_with_duplicates_at_end(self):
        assert Solution().containsDuplicate([10, 5, 3, 4, 3])

    def test_with_multiple_duplicates(self):
        assert Solution().containsDuplicate([10, 5, 5, 10, 4, 3, 2, 1, 2])

    def test_with_more_than_two_duplicates_of_given_element(self):
        assert Solution().containsDuplicate([10, 4, 10, 6, 8, 10])

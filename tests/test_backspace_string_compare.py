from src.backspace_string_compare.solution import Solution

class TestBackspaceStringCompare:
	def test_example_1(self):
		s,t = 'ab#c', 'ad#c'
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)

	def test_example_2(self):
		s,t = 'ab##', 'c#d#'
		assert Solution().backspaceCompare(s,  t)
		assert Solution().backspaceCompare(t, s)
	
	def test_example_3(self):
		s,t = 'a#c', 'b'
		assert not Solution().backspaceCompare(s, t)
		assert not Solution().backspaceCompare(t, s)

	def test_example_4(self):
		s,t = 'bxj##tw', 'bxo#j##tw'
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)

	def test_example_5(self):
		s,t = 'xywrrmp', 'xywrrmu#p'
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)

	def test_empty_strings(self):
		s,t = '####', ''
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)

	def test_string_starting_with_backspace(self):
		s,t = '####a#b', 'b'
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)

	def test_equivalent_strings_with_no_backspaces(self):
		s,t = 'abc', 'abc'
		assert Solution().backspaceCompare(s, t)
		assert Solution().backspaceCompare(t, s)
		
	def test_equivalent_strings_with_no_backspaces(self):
		s,t = 'abc', 'bc'
		assert not Solution().backspaceCompare(s, t)
		assert not Solution().backspaceCompare(t, s)
		
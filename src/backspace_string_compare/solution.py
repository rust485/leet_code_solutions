class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		i,j = len(s)-1, len(t)-1

		while i >= 0 or j >= 0:
			if i < 0 or j < 0:
				if i < 0:
					if t[j] == '#': j = self._backspace(j, t)
					else: return False
				else:
					if s[i] == '#': i = self._backspace(i, s)
					else: return False

			elif s[i] == '#' or t[j] == '#':
				if s[i] == '#': i = self._backspace(i, s)
				if t[j] == '#': j = self._backspace(j, t)

			elif s[i] != t[j]:
				return False
			
			else:
				i -= 1
				j -= 1
		
		return True

	def _backspace(self, idx: int, s: str) -> int:
		count = 0
		while idx > 0 and s[idx] == '#':
			count += 1
			idx -= 1

		return idx - count
class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		i,j = len(s)-1, len(t)-1
		skip_s = skip_t = 0

		while i >= 0 or j >= 0:
			i = self._backspace(i, s)
			j = self._backspace(j, t)

			if i < 0 and j < 0:
				break

			elif i < 0 or j < 0 or s[i] != t[j]:
				return False
				
			i -= 1
			j -= 1
		
		return True

	def _backspace(self, idx: int, s: str) -> int:
		skip = 0
		while idx >= 0:
			if s[idx] == '#': skip += 1
			elif skip > 0: skip -= 1
			else: break

			idx -= 1

		return idx
			
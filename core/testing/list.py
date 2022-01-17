from typing import Any, List

def lists_equal_unordered(l1: List[Any], l2: List[Any]):
	d1, d2 = {}, {}

	for v in l1:
		if v not in d1:
			d1[v] = 0
		d1[v] += 1
	
	for v in l2:
		if v not in d2:
			d2[v] = 0
		d2[v] += 1

	return d1 == d2
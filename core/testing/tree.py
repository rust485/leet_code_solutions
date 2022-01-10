from typing import Any, List, Optional


from core.model.treenode import TreeNode
from math import ceil

def build_tree(l: List[Any]) -> Optional[TreeNode]:
	if len(l) == 0:
		return None

	mp: List[TreeNode] = [None] * len(l)

	head = TreeNode(l[0])
	mp[0] = head

	for i in range(1, len(l)):
		if l[i] is None:
			continue

		n = TreeNode(l[i])

		p = mp[ceil(i / 2) - 1]

		if i % 2:
			p.left = n
		else:
			p.right = n
		
		mp[i] = n

	return head

def build_compact_tree(l: List[Any]) -> Optional[TreeNode]:
	if len(l) == 0:
		return None

	mp = [TreeNode(l[0])]

	j = 0
	for v in l[1:]:
		j += 1

		p = mp[ceil(j / 2) - 1]

		if v is None or p is None:
			mp += [None]
			continue

		n = TreeNode(v)

		if j % 2:
			p.left = n
		else:
			p.right = n
		
		mp += [n]

	return mp[0]
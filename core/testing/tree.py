from typing import Any, List, Optional


from core.model.treenode import TreeNode
from math import ceil

def build_tree(l: List[Any]) -> Optional[TreeNode]:
	"""
		Build a tree from a given list. With the value at index 0 being the root,
		the index of the parent for the value at index i = ceil(i / 2) - 1.

		Use None if a node should not be added for the given index.
	"""
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
	"""
	Build a tree from a list - this method mimics the tree builder 
	provided by leetcode, which allows for not specifying the children of 
	null nodes. 
	Example:
		Input: [1, 2, None, 3, None, 4]
				1
			   2
			  3
			 4

		Notice since the right node of the root is None, it is implied
		that the children of that non-existent node will also be none. 

		With build_tree, the input required to achieve the same output would be
		[1, 2, None, 3, None, None, None]
	"""
	if len(l) == 0:
		return None

	mp = [TreeNode(l[0])]

	i,j = 1,0
	while i < len(l):
		j += 1

		p = mp[ceil(j/2)-1]

		if p is None:
			mp += [None]
			continue

		v = l[i]
		if v is None:
			mp += [None]
		else:
			n = TreeNode(v)

			if j % 2:
				p.left = n
			else:
				p.right = n
			
			mp += [n]

		i += 1

	return mp[0]

def trees_are_equivalent(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
	"""
	Determine if 2 trees are equivalent - i.e. the same tree structure and the same 
	node values in both trees
	"""
	if not root1 and not root2:
		return True

	if root1 and not root2 or root2 and not root1 \
		or root1.val != root2.val:
		return False

	return trees_are_equivalent(root1.left, root2.left) and \
		trees_are_equivalent(root1.right, root2.right)
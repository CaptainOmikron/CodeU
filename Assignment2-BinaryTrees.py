
# Ancestors
'''
Apparently we can assume that
there are no duplicats (-> Slack)
'''
class tree:
	def __init__(self, rootval, left=None, right=None):
		self.rootval = rootval
		self.left = left #tree 
		self.right = right #tree

	def ancestors(self, key): # Q1
		if self.rootval == key:
			return True
		if self.left != None: 
			if self.left.ancestors(key):
				print(self.rootval)
				return True
		if self.right != None: 
			if self.right.ancestors(key):
				print(self.rootval)
				return True
		return False

	def contains(self, key): # is used by commonAncestor
		if self.rootval == key:
			return True
		if self.left != None: 
			if self.left.contains(key):
				return True
		if self.right != None: 
			if self.right.contains(key):
				return True
		return False

	def commonAncestor(self, key1, key2): # Q2
		if self.rootval == key1 or self.rootval == key2:
			print(self.rootval)
			return
		if self.left.contains(key1) and self.left.contains(key2):
			self.left.commonAncestor(key1, key2)
		elif self.right.contains(key1) and self.right.contains(key2):
			self.right.commonAncestor(key1, key2)
		else:
			print(self.rootval)


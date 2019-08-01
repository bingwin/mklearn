

class Soluttion:

	def invertTree(self, root):

		if root:
			print(root)
			root.left, root.right = root.right, root.left
			self.invertTree(root.left)
			self.invertTree(root.rigth)

		return root
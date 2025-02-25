I had a hard time with working on the tree_builder such as these code:

    root.left = self.build_from_pre_in(preorder[1:root_index+1], inorder[:root_index])

    root.right = self.build_from_pre_in(preorder[root_index+1:], inorder[root_index+1:])

I had to determin where to place the root_index and how it would work
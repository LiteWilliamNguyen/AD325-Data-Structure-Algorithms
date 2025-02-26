class TreeNode:
    def __init__(self,question):
        self.question = question
        self.left = None #Yes
        self.right = None   #No

def max_depth(root):
    if not root:
        return 0 #if the depth is 0, it is empty
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth,right_depth)+1 #adding 1 to current node
    
def build_tree():
    root = TreeNode("Do you need a loan?")

    root.left = TreeNode("Personal loan?")
    root.right = TreeNode("Need to look for investment?")

    root.left.left = TreeNode("Check credit score")
    root.left.right = TreeNode("Do you own property?")

    root.left.left.left = TreeNode("You are quality for Premium Loan")
    root.left.left.right = TreeNode("You are qualify for Standard Loan")

    root.left.right.left = TreeNode("Let's look through some mortgage option")
    root.left.right.right = TreeNode("Need more detail")

    root.right.left = TreeNode("Let's find some mutual fund")
    root.right.right = TreeNode("What about insurance plan?")

    root.right.left.left = TreeNode("We have some diverse mutual fund")
    root.right.left.right = TreeNode("We have some investment option")

    root.right.right.left = TreeNode("We have life insurance plan option")
    root.right.right.right = TreeNode("We have other coverage plan")

    return root
    
if __name__ == "__main__":
    final_tree_root = build_tree()
    print("Maximum depth: ", max_depth(final_tree_root))
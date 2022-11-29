# Hsuan-You Lin Module 8 Problem Set Question 6.

class LLRB_Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(node, num):
 
        if node is None:
            return (LLRB_Node(num))
     
        else:
            # 2. Otherwise, recur down the tree
            if num <= node.val:
                node.left = LLRB_Node.insert(node.left, num)
            else:
                node.right = LLRB_Node.insert(node.right, num)
     
            # Return the (unchanged) node pointer
            return node

    def Find_Minimum(root):
        while root.left is not None:
            root = root.left
        return root.val


if __name__ == "__main__":
    root = None
    root = LLRB_Node.insert(root, 3)
    LLRB_Node.insert(root, 9)
    LLRB_Node.insert(root, 10)
    LLRB_Node.insert(root, 4)
    LLRB_Node.insert(root, 6)
    LLRB_Node.insert(root, 5)
    
    print("\nThe minimun element: %d" % (LLRB_Node.Find_Minimum(root)))

# Hsuan-You Lin Module 8 Problem Set Question 7.

class LLRB_Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(node, num):
        if node is None:
            return (LLRB_Node(num))
        else:
            if num <= node.val:
                node.left = LLRB_Node.insert(node.left, num)
            else:
                node.right = LLRB_Node.insert(node.right, num)
            return node
            
    def Count_Nodes(root):
        count = 0
        if root is None:
            return count
     
        while (root != None):
            if (root.left == None):
                count+=1
                root = root.right
            else:
                pre = root.left
                while (pre.right != None and pre.right != root):
                    pre = pre.right
                if(pre.right == None):
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    count += 1
                    root = root.right
        return count

    def Find_Median(root):
        if root is None:
            return 0
        count = LLRB_Node.Count_Nodes(root)
        n = 0
     
        while (root != None):
            if (root.left == None):
                n += 1
                if (count % 2 != 0 and n == (count + 1) // 2):
                    return prev.val
                elif (count % 2 == 0 and n == (count // 2)+1):
                    return (prev.val + root.val) // 2
                root = root.right
            else:
                pre = root.left
                while (pre.right != None and pre.right != root):
                    pre = pre.right
                if (pre.right == None):
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    prev = pre
                    n += 1
                    if (count % 2 != 0 and n == (count + 1) // 2 ):
                        return root.val
     
                    elif (count % 2 == 0 and n == (count // 2) + 1):
                        return (prev.val + root.val)//2
                    n = root.right

if __name__ == "__main__":
    root = LLRB_Node(3)
    LLRB_Node.insert(root, 9)
    LLRB_Node.insert(root, 10)
    LLRB_Node.insert(root, 4)
    LLRB_Node.insert(root, 6)
    LLRB_Node.insert(root, 5)
    LLRB_Node.insert(root, 12)
    print("\nThe median element: %d" % (LLRB_Node.Find_Median(root)))

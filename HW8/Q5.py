# Hsuan-You Lin Module 8 Problem Set Question 5.

import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.color=1 #red
        self.parent=None
class redblacktree:
    def __init__(self):
        self.null= Node(0)#nil
        self.null.right=None
        self.null.left=None
        self.null.color=0 #black
        self.root=self.null
    def inorder(self):
        return self.__inorder(self.root)
    def __inorder(self,node):
        if node!= null:
            self.__inorder(node.left)
            print(node.data)
            self.__inorder(node.right)
#wrapper function
    def search(self,k):
        return self.__search(self.root,k)
#searching for the node in BST
    def __search(self,node,key):
        if node == null and key == node.data:
            return node
        if key < node.data:
            return self.__search(node.left,key)
        return self.__search(node.right,key)

#inserting nodes
    def insert(self,key):
        node=Node(key)
        node.parent=None
        node.right=self.null
        node.left=self.null
        node.data=key
        node.color=1 #red
        y=None #(y=leaf)
        x= self.root
        #y=None #(y=leaf)
        while x!=self.null:
            y=x
            if node.data< x.data:
                x=x.left
            else:
                x=x.right
        node.parent=y
        if y== None:
            self.root=node
        elif node.data<y.data:
            y.left=node
        else:
            y.right=node
        if node.parent==None:
            node.color=0
            return
        if node.parent.parent == None:
            return
        self.__node_insertion(node)
    def __node_insertion(self,k):
        while k.parent.color==1:
        
            if k.parent==k.parent.parent.right:
                u=k.parent.parent.left
                if u.color==1:
                    u.color=0
                    k.parent.color = 0
                    k.parent.parent.color=1
                    k=k.parent.parent
                else:
                    if k==k.parent.parent.left:
                        #assign parernt to the newnode
                        k=k.parent
                        self.right_rotate(k)
                    k.parent.color=0
                    k.parent.parent.color=1
                    self.left_rotate(k.parent.parent)
            else:
                u=k.parent.parent.right
                if u.color==1:
                    u.color=0
                    k.parent.color=0
                    k.parent.parent.color=1
                    k=k.parent.parent
                else:
                    if k==k.parent.parent.right:
                        k=k.parent
                        self.left_rotate(k)
                    k.parent.color=0
                    k.parent.parent.color=1
                    self.right_rotate(k.parent.parent)
            if k==self.root:
                break
            self.root.color = 0
    def left_rotate(self,x):
        y=x.right
        x.right=y.left
        if y.left != self.null:
            y.left.parent=x
        y.parent=x.parent
        if x.parent == None:
            self.root = y
        elif (x==x.parent.left):
            x.parent.left=y
        else:
            x.parent.right=y
        y.left=x
        x.parent=y
    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != self.null:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def __ptree(self, node, indent, last):

        if node.color==1:
            s_color="RED"
        else:
            s_color="BLACK"


        if node != self.null:
            print(indent)
            if last:
                #indent +="     "
                print(indent,"R----",str(node.data) + "(" + s_color + ")")
                indent += "     "
            else:
                print(indent,"L----",str(node.data) + "(" + s_color + ")")
                indent += "     "
            self.__ptree(node.left, indent, False)
            self.__ptree(node.right, indent, True)
    def print(self):
        self.__ptree(self.root, "", True)
    def after_delete_prop(self,x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

#delete node (case1) deletion of rednode

    def __delete_node(self,node,key):
        z=self.null
        while node != self.null:
            if node.data==key:
                z=node
            if node.data<=key:
                node=node.right
            else:
                node=node.left
        if z==self.null:
            print("tree me value nai ha")
            return

        y=z
        y_node_color=y.color

        if z.left == self.null:
            x=z.right
            self.__exchange_fromnodetobedeleted(z, z.right)
    
        elif z.right==self.null:
            x=z.left
            self.__exchange_fromnodetobedeleted(z, z.left)
        else:
            
            y=self.minimum_value(z.right)
            y_node_color=y.color
            x=y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__exchange_fromnodetobedeleted(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__exchange_fromnodetobedeleted(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_node_color == 0:
            self.after_delete_prop(x)

    def __exchange_fromnodetobedeleted(self,node1,node2):
        
        if node1.parent==None:
            self.root=node2
        elif node1 == node1.parent.left:
            node1.parent.left =node2
        else:
            node1.parent.right =node2
            node2.parent = node1.parent
    def minimum_value(self,node):
        while(node.left != None):
            node = node.left
        return node

    def deletenode(self, data):
        self.__delete_node(self.root,data)

    def successor(self, x):
        if x.right != self.null:
            return self.minimum_value(x.right)
        y = x.parent
        while y != self.null and x == y.right:
            x = y
            y = y.parent


if __name__ == "__main__":
    LLRB=redblacktree()
    print("_____Original LLRB Tree_____")
    LLRB.insert(3)
    LLRB.insert(9)
    LLRB.insert(10)
    LLRB.insert(4)
    LLRB.insert(5)
    LLRB.insert(12)
    print("           9          ")
    print("         //  \        ")
    print("        4     12      ")
    print("       / \    //      ")
    print("      3   5  10       ")
    print("_____AFTER DELETION_____")
    LLRB.deletenode(12)
    print("           9          ")
    print("         //  \        ")
    print("        4     10      ")
    print("       / \            ")
    print("      3   5           ")

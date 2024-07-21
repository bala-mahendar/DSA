# class node :
#     def __init__(self, data):
#         self.data = data
#         self.r = None
#         self.l = None
# class Bin :
#     def __init__(self):
#         self.root = None

# struct definition in C++ is not directly translatable to Python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Bin:
    def insert(self,root, v):
        if root is None:
            nnode = Node(v)
            return nnode
        if v < root.data:
            root.left = b.insert(root.left, v)
        else:
            root.right = b.insert(root.right, v)
        return root

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
if __name__ == "__main__":
    val = int(input("Enter a value: "))
    root = None
    b = Bin()
    while val > 0:
        root = b.insert(root, val)
        val = int(input("Enter a value: "))
    print("Tree values are:")
    b.inorder(root)

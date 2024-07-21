# class node:
#     def __init__(self, data):
#         self.data = data
#         self.nxt = None

# class llist:
#     def __init__(self):
#         self.head = None

#     def front(self, data):
#         nnode = node(data)     
#         if self.head is None:
#             self.head = nnode
#         else:
#             nnode.nxt = self.head
#             self.head = nnode

#     def printer(self):
#         if self.head is None:
#             print("List is empty")
#         else:
#             temp = self.head
#             while temp:
#                 print(temp.data)
#                 temp = temp.nxt

# if __name__ == '__main__':
#     list1 = llist()
#     inp = int(input("Enter the number of values: "))
#     for _ in range(inp):
#         s = int(input())
#         list1.front(s)
#     list1.printer()


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def addany(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element,end='-->')
            p = p._next
        print()

    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                print(index)
            p = p._next
            index = index + 1
        else: print("Doesn't exist !!!")

    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        if self.isempty():
            self._tail = None
        return e
L = LinkedList()
inp = int(input("Enter the number of values: "))
for _ in range(inp):
        s = int(input())
        L.addlast(s)
L.display()
d  =int(input("Enter key to search : "))
L.search(d)
L.removefirst()
L.display()
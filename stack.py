# class stack:
#     def __init__(self):
#         self.data = []
#     def isempty(self):
#         if not self.data: return True 
#         # else :return False
#     def add(self,data):
#         self.data.append(data)
#     def top(self):
#         print(self.data[-1])

#     def diplay(self):
#         for i in self.data:
#             print(i,end=" ")

#     def pop(self):
#         if self.isempty():
#             print("List is Empty")
#             return
#         del self.data[-1]
        
# if __name__ == '__main__':
#     s = stack()
#     values = int(input("Enter times : "))
#     for _ in range(values):
#         d = int(input())
#         s.add(d)
#     s.diplay()
#     print()
#     s.pop()
#     s.diplay()

class node:
    def __init__(self,data):
        self.data= data
        self.next = None
        # self.prev = None
class Stack:
    def __init__(self):
        self.head = None
        self.len = 0
        # self.tail = None

    def push(self):
        data = int(input())
        nnode = node(data)
        if self.head == None:
            self.head = self.tail = nnode
        else:
            nnode.next = self.head
            self.head = nnode
        self.len +=1

    def isempty(self):
        return self.len == 0

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return 
        else:
            temp = self.head.data
            self.head = self.head.next
            temp = None
        self.len-=1
    
    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            p = self.head
            while p:
                print(f"==============\n||    {p.data}     ||\n=============")
                p=p.next

if __name__ == '__main__':
    user = int(input("Enter STACK Capacity : "))
    s = Stack()
    for i in range(user):
        s.push()
    s.pop()
    s.display()
    

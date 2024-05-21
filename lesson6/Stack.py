import Node
class Stack:
    def __init__(self):
        self.head = Node.Node("Head")
        self.size = 0

    def IsEmpty(self):
        return self.size == 0

    def Pop(self):
        if self.IsEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head
        self.head = self.head.next
        self.size -= 1
        return remove.value

    def Push(self, value):
        try:
            node = Node.Node(int(value))
        except ValueError:
            print("you can't enter a string")
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    #         except ValueError:
    #             print("can't enter a string")

    def Peek(self):
        return self.head.value


#stack = Stack()
#stack.Push(input("enter a number"))
# for i in range(11, 21):
#     stack.Push(i)
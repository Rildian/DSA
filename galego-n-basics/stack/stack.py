from node import Node


class Stack:
    
    def __init__(self):
        self.head = None
        self._size = 0


    def size(self) -> int:
        return self._size
    

    def put(self, node: object):
    
        top = Node(node)
        top.next = self.head
        self.head = top

        self._size += 1

    def pop(self):
        aux = self.head.next
        self.head = aux
        

    def printStack(self):
        
        aux = self.head
        while (aux):
            print(aux.data)
            aux = aux.next
    
    def top(self):
        return self.head.data
    

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        return False


    def clear(self) -> None:
        aux = self.head
        while (aux):
            aux = aux.next
        
        self.head = aux

    def copy(self) -> None:
        copycat = self.head


    def contains(self, item) -> bool:
        
        if self.head.data == item:
            return True
        
        aux = self.head
        
        while (aux.next):
            aux = aux.next
            if aux.data == item:
                return True
        
        if aux.next == None and aux.data != item:
            return False

stack = Stack()

stack.put(20)
#print(stack.size())
stack.put(10)
stack.printStack()
stack.put(30)

print(stack.contains(30))

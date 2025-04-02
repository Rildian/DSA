from node import Node

class Stack:
    
    def __init__(self):
        self.topo = None
        self._size = 0


    def size(self) -> int:
        return self._size
    

    def put(self, node: object):
    
        aux = Node(node)
        aux.next = self.topo
        self.topo = aux

        self._size += 1


    def pop(self):
        aux = self.topo.next
        self.topo = aux
        

    def printStack(self):
        
        aux = self.topo
        while (aux):
            print(aux.data)
            aux = aux.next
    

    def top(self):
        return self.topo.data if self.topo else None
    

    def isEmpty(self) -> bool:
        return True if self.topo is None else False


    def clear(self) -> None:
        aux = self.topo
        while (aux):
            aux = aux.next
        
        self.topo = aux


    def copy(self) -> None:
        copycat = self.topo


    def contains(self, item) -> bool:
        
        if self.topo.data == item:
            return True
        
        aux = self.topo
        
        while (aux.next):
            aux = aux.next
            if aux.data == item:
                return True
        
        if aux.next == None and aux.data != item:
            return False

stack = Stack()
stack.put(30)
stack.put(20)
stack.put(10)
print(stack.contains(30))
stack.printStack()
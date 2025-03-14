from node import Node

class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    
    def size(self) -> int:
        return self._size


    def insertOnRear(self, node: object) -> None:
        if self.first == None:
          self.first = Node(node)
          self.last = Node(node)
        else:
            self.last = Node(node)
            self.first.next = self.last
        
        self._size += 1
    

    def delete(self):
        self.first = self.first.next
        
        self._size -= 1
    

    def printQueue(self) -> None:
        aux = self.first
        while (aux):
            print(aux.data, end=" -> " if aux.next else "")
            aux = aux.next


    def getLast(self):
        return self.last.data
    

    def getFirst(self):
        return self.first.data


    def isEmpty(self):
        return True if self.first is None else False
    

queue = Queue()
queue.insertOnRear(10)
queue.insertOnRear(20)
print(queue.size())
queue.delete()
print(queue.size())

queue.delete()
print(queue.size())

queue.delete()
print(queue.size())
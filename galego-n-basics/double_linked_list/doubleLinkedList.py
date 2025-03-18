class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def getSize(self) -> int:
        return self._size

    
    def getHead(self):
        return self.head.data

    
    def getTail(self):
        return self.tail.data


    def insertOnHead(self, node: object):
        aux = NodeDLL(node)

        if self.head is None:
            self.head = aux
            self.tail = aux
        else:
            self.head.prev = aux
            aux.next = self.head
            self.head = aux
        
        self._size += 1


    def insertOnTail(self, node: object):
        aux = NodeDLL(node)
        self.tail.next = aux
        aux.prev = self.tail
        self.tail = aux

        self._size += 1
    

    def insertOnMiddle(self, node: object, index: int):
        if index < 0 or index > self._size:
            raise IndexError("Invalid index")
        
        aux = NodeDLL(node)
        
        if index == (self._size): #tail
            self.tail.next = aux
            aux.prev = self.tail
            self.tail = aux
        elif index == (self._size-1): # before tail
            aux.next = self.tail
            aux.prev = self.tail.prev
            self.tail.prev.next = aux
            self.tail.prev = aux
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            aux.next = curr.next
            aux.prev = curr
            aux.next.prev = aux
            curr.next = aux
        

        self._size += 1

    
    def deleteHead(self):
        self.head = self.head.next
        
        self._size -= 1

    
    def deleteTail(self):
        self.tail = self.tail.prev
        self.tail.next = None

        self._size -= 1


    def deleteMiddle(self, index: int):
        past = self.head
        
        for i in range(index-1):
            past = past.next
        
        past.next = past.next.next
        past.next.prev = past

        self._size -= 1
    

    def searchElement(self, elem: int):
        aux = self.head
        index = 0
        while (aux):
            if aux.data == elem:
                return index
            
            index += 1
            aux = aux.next

        if not aux:
            raise IndexError("Element not found")
    

    def search(self, index):
        if (index < 0 or index > self._size):
            raise IndexError("Invalid index")
        
        aux = self.head
        for i in range(index):
            aux = aux.next
        
        if aux:
            return aux.data
        
        raise IndexError("Element not found")
        

    def deleteThisElement(self, elem: int):
        aux = self.head
        curr = self.head

        while (aux):
            if aux.data == elem:
                aux.prev.next = aux.next
                aux.next = aux.prev
                
                self._size -= 1
                return

            aux = aux.next

        raise IndexError("This element doesn't exist")

    
    def deleteThisIndex(self, index: int):
        if (index < 0 or index > self._size):
            raise IndexError("Invalid index")

        aux = self.head
        i = 0
        while (aux):
            if i == index:
                aux.next.prev = aux.prev
                aux.prev = aux.next
                self._size -= 1

                return
            aux = aux.next
        
        raise IndexError("Theres no element in this index")


    def isEmpty(self):
        return True if self.head is None else False
    

    def extends(self, elements: list):
        for i in range(len(elements)):
            self.insertOnTail(i)
    

    def removeAll(self):
        self.head = None
        self.tail = None


    def printDoubleLinkedList(self):
        aux = self.head
        while aux:
            print(aux.data, end=" <-> " if aux.next else " ->  ")
            aux = aux.next
        print("\n")


dLL = DoubleLinkedList()

dLL.insertOnHead(10)
dLL.insertOnTail(20)
dLL.insertOnTail(30)
dLL.printDoubleLinkedList()

dLL.insertOnMiddle(10, 1)

dLL.printDoubleLinkedList()
print(dLL.getSize())
dLL.insertOnMiddle(33, 4)
dLL.printDoubleLinkedList()
print(dLL.getSize())
dLL.insertOnMiddle(66, 4)
print(dLL.getSize())
dLL.printDoubleLinkedList()


            


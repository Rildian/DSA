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
        aux = NodeDLL(node)
        
        if index == (self._size-1):
            aux.next = self.tail
            aux.prev = self.tail.prev
            self.tail.prev = aux

        curr = self.head
        for i in range(index-1):
            curr = curr.next
        
        aux.next = curr.next # o aux "empurra, ele aponta pro indice atual"
        curr.next = aux # o "indicee atual" se torna o aux
        aux.prev = curr # o curr (que tá atras do indice desejado) se torna prev
        aux.next.prev = aux

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
dLL.insertOnTail(40)
dLL.insertOnHead(5)
dLL.insertOnMiddle(69, 3)
dLL.insertOnMiddle(80, 3)
dLL.printDoubleLinkedList()

print(dLL.getSize())

dLL.insertOnMiddle(1, 6)
dLL.printDoubleLinkedList()
print(dLL.getSize())
dLL.insertOnMiddle(75, 7)
dLL.deleteTail()
dLL.deleteMiddle(2)
dLL.printDoubleLinkedList()
print(dLL.search(2))
print(dLL.searchElement(80))
dLL.deleteThisElement(80)
dLL.printDoubleLinkedList()
            


from node import Node



class ExceptionListElementNotFound(Exception):
    def __init__(self, element, message=f"Element not found on this linked list"):
        self.element = element
        self.message = message
        super().__init__(self.message)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0 # esse underscore no começo pra sinalizar que não eh pra mexer nisso

    def insertOnTail(self, node: object):

        if self.head: # se ja tiver elemetos
            aux = self.head
            while(aux.next is not None):
                aux = aux.next
            aux.next = Node(node)
        else:
            self.head = Node(node) # criar o 1o elemento
        
        self._size += 1
    
    def insertOnThisIndex(self, index: int, element):
        
        if index == 0 or self.head is None:
            self.head = Node(element)
        if index > self._size or index is None or index < 0:
            raise IndexError("Invalid position to insert.")

        i = 0
        aux = self.head
        while aux is not None:
            aux = aux.next
            i += 1
            if i == index:
                aux.data = element
                break

    def length(self) -> int:
        return self._size
    
    
    def index(self, index : int):
        aux = self.head
        
        if self.head is None:
            raise IndexError("The list is empty")
        
        if index < 0 or index > self._size:
            raise IndexError("Invalid index")

        if index == 0:
            return self.head.data
        
        for i in range(index):
            if aux:
                aux = aux.next
            else:
                raise IndexError("index out of range lolz")
        
        if aux:
            return aux.data
        

    def searchTheElement(self, element):
        index = 0
        aux = self.head
        while (aux): # enquanto n for none
            if aux.data == element:
                return index
            
            aux = aux.next
            index += 1

        return ExceptionListElementNotFound(element)


    def removeIndex(self, index: int):
        if index < 0 or index >= self._size:  
            raise IndexError("Invalid index")

        if index == 0:
            self.head = self.head.next
        else:
            aux = self.head
            for i in range(index-1):
                aux = aux.next
            aux.next = aux.next.next if aux.next else None

        self._size -= 1

        

    def removeElement(self, element: int):
        if self.head is None:
            return 

        if self.head.data == element:
            self.head = self.head.next

        prev = self.head
        aux = self.head.next

        while (aux):
            if aux.data == element:
                prev.next = aux.next
                break
            aux = aux.next
            prev = prev.next           

            if aux.next == None and aux.data != element:
                self._size += 1
                raise ExceptionListElementNotFound(element)

        aux = prev

        self._size -= 1

    def printList(self):
        aux = self.head
        while aux:
            print(aux.data, end=" -> " if aux.next else " ->  ")
            aux = aux.next
    

# some examples bellow, you can try it by yourself

lista = LinkedList()
lista.insertOnTail(10)
lista.insertOnTail(20)
lista.insertOnTail(30)
lista.insertOnTail(40)
lista.insertOnTail(50)

lista.printList()
print("\n")
print(lista.length())

#lista.removeElement(70)

print(lista.length())
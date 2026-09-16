class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        current = self.head
        while current != None:
            if index == 0:
                return current.value
            current = current.link
            index -= 1
        return -1

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val, temp)


    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None)
            return

        current = self.head
        while current != None:
            if current.link == None:
                current.link = Node(val, None)
                return
            current = current.link
        

    def remove(self, index: int) -> bool:
        current = self.head
        previous = None
        while current != None:
            if index == 0:
                if previous == None:
                    if self.head.link == None:
                        self.head = None
                    else:
                        self.head = self.head.link
                else:
                    previous.link = current.link
                return True
            previous = current
            current = current.link
            index -= 1
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current != None:
            values.append(current.value)
            current = current.link
        return values
        
class Node:
    def __init__(self, value, link):
        self.value = value
        self.link = link
    
    def __str__(self):
        return f"self: {self.value}, next: {self.link.value if self.link else None}"
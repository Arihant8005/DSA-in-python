class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Singly_linked_list:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = new_node
    
    def Travesel(self):
        if(self.head == None):
            print("Empty")
        else:
            current = self.head
            while(current is not None):
                print(current.val, end = " ")
                current = current.next

    def Insert_at(self, val, pos):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while(current is not None and count < pos):
                prev = current
                current = current.next
                count += 1
            prev.next = new_node
            new_node.next = current
            
SLL = Singly_linked_list()
SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(50)
SLL.Insert_at(100, 3)
SLL.Travesel()
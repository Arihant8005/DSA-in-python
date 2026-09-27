class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None

    def Append(self, val):
        new_node = Node(val)
        if(self.head == None):
            self.head = new_node
        else:
            curr = self.head
            while(curr.next is not None):
                curr = curr.next
            curr.next = new_node

    def Travesel(self):
        if(self.head == None):
            print("single linked list is empty")
        else:
            current = self.head
            while(current is not None):
                print(current.val, end = " ")
                current = current.next

SLL = singly_linked_list()
SLL.Append(10)
SLL.Append(20)
SLL.Append(30)
SLL.Append(40)
SLL.Append(50)
SLL.Travesel()
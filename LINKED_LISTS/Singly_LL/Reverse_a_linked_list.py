# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def Append(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next is not None:
                curr = curr.next

            curr.next = new_node

    def Travesel(self):
        current = self.head

        while current is not None:
            print(current.val, end=" ")
            current = current.next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev


# Create linked list
SLL = LinkedList()

SLL.Append(10)
SLL.Append(20)
SLL.Append(30)
SLL.Append(40)
SLL.Append(50)

print("Original:", end=" ")
SLL.Travesel()

# Reverse linked list
solution = Solution()
middle = solution.reverseList(SLL.head)

print("\nReverse:", end=" ")

current = middle
while current is not None:
    print(current.val, end=" ")
    current = current.next
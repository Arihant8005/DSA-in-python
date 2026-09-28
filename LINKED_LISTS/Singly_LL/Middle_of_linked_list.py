# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

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
    def middleNode(self, head):
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow


# Create linked list
SLL = LinkedList()

SLL.Append(10)
SLL.Append(20)
SLL.Append(30)
SLL.Append(40)
SLL.Append(50)

SLL.Travesel()

# Find middle
solution = Solution()
middle = solution.middleNode(SLL.head)

print("\nMiddle:", middle.val)
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def __str__(self):
    return str(self.val)

head = tail = DoublyNode(1)
print(tail)

# Display - O(n)
def display(head):
    curr = head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))
displa

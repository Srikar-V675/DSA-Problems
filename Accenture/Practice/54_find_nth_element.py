# Find Nth Element in Linked List
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

def findNth(head: Node, n: int) -> int:
    count = 0
    temp = head
    while temp and count < n:
        temp = temp.next
        count += 1
    return temp.data
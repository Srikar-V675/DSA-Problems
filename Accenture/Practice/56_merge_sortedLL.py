# Merge 2 Sorted Linked Lists
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
    

def mergeSortedLL(head1: Node, head2: Node) -> Node:
    dummy = Node(0)
    cur = dummy
    temp1 = head1
    temp2 = head2
    
    while temp1 and temp2:
        if temp1.data <= temp2.data:
            cur.next = temp1
            temp1 = temp1.next
        else:
            cur.next = temp2
            temp2 = temp2.next
    
    if temp1:
        cur.next = temp1
    
    if temp2:
        cur.next = temp2
    
    return dummy.next
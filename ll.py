class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def revUnique(head):
    prev = head
    cur = head.next
    space = 1
    var = prev 
    
    while cur:
        old = var 
        prev = cur
        cur = cur.next
        var = prev
        for _ in range(space):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        old.next = prev
        if not cur:
            var.next = None
            break
        space += 1
    
    return head

# create ll: a->b->c->d->e->f
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

head = revUnique(a)

while head:
    print(head.value)
    head = head.next       
class Node(object):
    def __init__(self,data = None,next_node= None):
        self.data = data
        self.next = next_node
    def setNext(self, next_node = None):
        self.next = next_node


def _isCycle(head):
    if head == None:
        return False
    nodo = head
    while nodo or head or head.next:
        if not head.next:
            return False

        if nodo == head.next or nodo == head.next.next:
            return True

        nodo = head.next
        head= head.next.next

    return False
    

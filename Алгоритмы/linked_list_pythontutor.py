class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    
    def __repr__(self) -> str:
        return f"{self.data}"

def print_linked_list(head):
    while head is not None:
        print(head)
        head = head.next
 
def build_linked_list(elements):
    head = None
    current = None
    previous = None
    for element in elements:
        current = Node(element, None)
        if head is None:
            head = current
            previous = current
        else:
            previous.next = current
            previous = current
    return head

head = build_linked_list ([5,10,15,7,3,1])


print_linked_list(head)
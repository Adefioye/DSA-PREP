class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# def reverseLinkedList(head):

#     if head == None or head.next == None:
#         return head 

#     p = reverseLinkedList(head.next)

#     head.next.next = head 
#     head.next = None 

#     return p

def reverseLinkedList(head, prev=None):
    if head == None:
        return prev
    next = head.next
    head.next = prev 
    return reverseLinkedList(next, head)

head.print_list()
result = reverseLinkedList(head)
result.print_list()
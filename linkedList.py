# We want to create a singly LinkedList class
# We want our LInkedList class to have one method called `add`
# The add method takes one parameter called `value`. The value is always appended to the end of the LinkedList
# We do not care the type of value, anything can be added
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            # Case1: LL is empty
            self.head = Node(value)
            self.tail = self.head
        else:
            # Case2: LL is not empty
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)

linked_list.print()
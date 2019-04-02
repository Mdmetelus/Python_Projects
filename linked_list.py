class Node:
    def __init__(self, value, next_node):
        # its own value
        self.value = value
        # the next node in the list (pointer)
        self.next_node = next_node

    def get_Value(self):
        # return the value of this node
        return self.value

    def get_next(self):
        # return a reference to this nodes next_node property
        return self.next_node

    def set_next(self, new_next):
        # ser this node's next_node property
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference the first noe in the linked list
        self.head = None
        # reference to the last node in the linked list
        self.tail = None

    # add a new node to the tial of our list
    def add_to_tail(self, value):
        new_node = Node(value)
        # we have an empty linked list
        # check the head referece
        if self.head is None and self.tail is None:
            # both self.head and self.tail to point
            # to the new node we'll add
            self.head = new_node
            self.tail = new_node
        # every othe case

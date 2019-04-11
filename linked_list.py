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
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    
    # remove and return the value o the head node
    def remove_from_head(self):
        # make sure our list isn't empty
        if not self.head and not self.tail:
                return None
        # take anonther reference to the head we're
        # about to delete
        old_head_value = self.head.value
        # we only have a single node in the list
        if self.head is self.tail:
                self.head = None
                self.tail = None
                return old_head_value
        # we have at least two nodes in the list
        else:
                # move the self.head reference to refer to the old head's next node
                self.head = self.head.get_next()
                return old_head_value
        
    def contains(self, target):
        # make sure we dont have an empty list
        if not self.head and not self.tail:
            return false
        # init a current reference to refer to the current node we're itereating on
        current = self.head
        #while the current node in the list is a valid Node
        while current:
                #check if the current node's value matches what we're looking for
                if current.value == target:
                    return True
                # update the current reference to the next node in the list
                current = crrent.get_next()
        # we've traversed the entire list
        return False

                

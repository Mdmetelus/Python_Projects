from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self, init=None):
        self.content = DoublyLinkedList()
        if init !=None:
            for char in init:
                self.contents.add_to_tail(char)

    def __len__(self):
        return len(self.content)

    def __str__(self):
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, char):
        self.contnets.add_to_tail(char)

    def prepend(self, char):
        self.contents.add_to_head(char)

    def delete_front(self):
        self.contents.remove_from_head()

    def delete_back(self):
        self.contents.remove_from_tail()

    def join(self, buffer):
        buffer.contents.head.prev = self.contents.tail
        self.contents.tail.next = buffer.contents.head
        self.contents.tail = buffer.contents.tail
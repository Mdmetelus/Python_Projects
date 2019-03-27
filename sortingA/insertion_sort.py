class Book:
    title = "title"
    author = "last, first"
    genre = "fiction"

    def __init__(self, t, a, g):
        self.title = t
        self.author = a
        self.genre = g

    def__repr__(self):
        return str(self.genre) + ": " + str(self.title) + " by " + str(self.author)

def insertion_sort(books):
    for i in range(1, len(books)):
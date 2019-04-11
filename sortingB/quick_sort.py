from book import Book
import time
import csv

def quick_sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x.title.lower() < pivot.title.lower():
                less.append(x)
            elif x.title.lower() == pivot.title.lower():
                equal.append(x)
            else: 
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

with open('book_data.csv') as csvfile:
    my_books = []
    data = csv.DictReader(csvfile)
    for book in data:
        my_books.append(Book(book['title'], book['author'], book['genre']))

start = time.time()
sorted_books = quick_sort(my_books)
print (type(sorted_books))
end = time.time()
print("Quick Sort took:      " + str((end - start)*1000) + " milliseconds")

for book in sorted_books:
    print(str(book)+"\n")
print("\n***SORTED books***")
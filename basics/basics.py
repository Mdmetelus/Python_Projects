address = ["Flat floor Street", "18", "NewYork"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1])

pin = int(input("Enter your pin: "))
def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.split

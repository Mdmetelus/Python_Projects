address = ["Flat floor Street", "18", "NewYork"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1])

pin = int(input("Enter your pin: "))
def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "That Fruit is in the List."
    else:
        return "No such fruit found!"
    
if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!")
    print("This info can be accsessed only by: ")
    for key in pins.keys():
        print(key)
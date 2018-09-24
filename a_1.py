#
#This is a simple program  to create a block.
#
#


'''
bChain = [1, 8.6, 5.1]
bChain.append(10)
bChain.append(3)
bChain.pop()
'''

boomChain = []

def add_value():
    boomChain.append(5.3)
    print(boomChain)
add_value()
add_value()
add_value()
add_value()


bingChain =[1]

def add_value1():
    bingChain.append([bingChain[-1], 5.3])
    print(bingChain)
add_value1()
add_value1()
add_value1()

bingoChain =[1]

def add_value2(transaction_amount):
    bingoChain.append([bingoChain[-1], transaction_amount])
    print(bingoChain)
add_value2(2)
add_value2(0.9)
add_value2(12.75)

bongoChain =[1]

def add_value3(transaction_amount):
    bongoChain.append([bongChain[-1], transaction_amount])
    print(bongoChain)
add_value3(2)
add_value3(0.9)
add_value3(12.75)


bungoChain =[1]

def get_last_bungoChain_value():
    return bungoChain[-1]


def add_value4(transaction_amount):
    bungoChain.append([get_last_bungoChain_value(), transaction_amount])


    add_value4(2)
    add_value4(0.9)
    add_value4(12.75)

    print(bungoChain)

add_value4()

bengoChain = []

def get_last_bungoChain_value():
    return bengoChain[-1]


def add_value5(transaction_amount, last_transaction):
    bengoChain.append([last_transaction,transaction_amount])

    add_value5(2,[1])
    add_value5(0.9, get_last_bungoChain_value())
    add_value5(13.9, get_last_bungoChain_value())

    print(bengoChain)
add_value5()

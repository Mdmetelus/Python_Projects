bingoChain =[]

def get_last_bingoChain_value():
    return bingoChain[-1]


def add_Value(transaction_amount, last_transaction =[1]):
    bingoChain.append([ last_transaction, transaction_amount])

    tx_amount = float(input("What amount would you like to put now? "))
    add_Value(tx_amount)
    tx_amount = float(input("What amount would you like to put now? "))
    add_Value(last_transaction=get_last_bingoChain_value(), transaction_amount=tx_amount)
    tx_amount = float(input("What amount would you like to put now? "))
    add_Value(tx_amount, get_last_bingoChain_value())
    tx_amount = float(input("What amount would you like to put now? "))
    add_Value( tx_amount, get_last_bingoChain_value())

    print(bingoChain)

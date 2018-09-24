#
#
#
#
#I'd like to print out a conversation between 2 people where each print out also promts a responce to the last statmentself.
#each statment is saved toy the last aray and the next statment will be added to the end of the arrayself.




chatChain =[, ]

def get_last_chatChain_valueb():
    return chatChain[,-1]


def get_last_chatChain_valuea():
    return chatChain[-1, ]


def add_Value(transaction_amount, last_transaction =[1]):
    bingoChain.append([ last_transaction, transaction_amount])


def add_Value(transaction_amount, last_transaction =[1]):
    bingoChain.append([ last_transaction, transaction_amount])


def get_user_input():
    return string(input("What amount would you like to put now? ")) #must convert to a string

    tx_amount = get_user_input()
    add_Value(tx_amount)
    tx_amount = get_user_input()
    add_Value(last_transaction=get_last_bingoChain_value(), transaction_amount=tx_amount)
    tx_amount = (tx_amount)
    add_Value(tx_amount, get_last_bingoChain_value())
    tx_amount = (tx_amount)
    add_Value( tx_amount, get_last_bingoChain_value())

    print(bingoChain)

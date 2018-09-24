# A simple program to.....
#
# Max David Metelus
# Date:

def main():
    a = input("what is your name?  ")
    print('Hello to you, '+ a)

#ask the user to store 2 vales and store them in memory.
#convert the srings into regular nombers integers
    num1, num2 = input( a +', Please enter two numbers: ').split()
    num1 = int(num1)
    num1 = int(num2)
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    remainder = num1 % num2
    power = num1 ** num2


    print("{} + {} = {}".format(num1, num2, sum))
    print("{} - {} = {}".format(num1, num2, difference))
    print("{} * {} = {}".format(num1, num2, product))
    print("{} / {} = {}".format(num1, num2, quotient ))
    print("{} % {} = {}".format(num1, num2, remainder))
    print("{} ** or ^ {} = {}".format(num1, num2, power))

main()

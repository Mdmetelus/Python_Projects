# A simple program to illustrate caotic behavior
def main():
    print('This Program illustrates a chaotic Function')
    x = eval(input('Enter a number between 0 and1 : '))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()

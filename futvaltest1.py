# futvaltest1.py
# A Simple program to compute the future value
# Illustrates the use of multiple inputs.
# Max David Metelus

def main():
    
    print("This program computed the Future Value.")
   
    principle = eval(input("How much will you put in the Bank?  "))
    
    apr = eval(input("How Much is the Bank going to give you as as Annual Rate?  "))

    z = eval(input("How many years will this amount Rest in the Banks Hands?  "))

    for i in range(z):
        principle = principle *(1 + apr)
        # how can you round to 2 decimanl places?? Find out
    print("Your ending total will be:", str(principle))

main()

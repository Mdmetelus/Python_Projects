# Grading System Grades.py
# A simple program to keep grades and calculate averages for students by treachers.
# It Illustrates the use of Multiple 
# Max David Metelus

#import statistics as stat

# Login:
'''xx = 0
While xx != 'MembersOnly':
    x = input(print("What is the Password?  ")'''
    
# end of login_____________________________________________________________________
def main():
    print("A simple program to keep grades and calculate averages for students by treachers.")
    z = 0
    y = 'Who'
    x = 'Grade'
    n = None
    close = n

    students = {'Tom': [97, 67, 89,],
                'Dick': [76, 85, 75,],
                'Harry': [78, 88, 98,],
                'Jon':[ 88, 94, 98,]}
    #print("OK")



    print("Welcone to Grade Central\n [1] - Enter grades \n [2] - Remove students \n [3] - Students Average Grades \n [4] - Exit \n [5] - Add A Student \n [6] - Veiw Students Grades\n")
    print(students)
    z = eval(input(print("What Would you like to do Today? (Enter a Number Here):  ")))
    if z == 1 :
        y = str(input("Student Name:  "))
        x = eval(input("Please put " + str(y)+ "'s grade in here:  "))
        def addsSudentGrade():
            if y in students:
                y.insert(x)
                students[y].append(int(x))
                print("Adding Grade..." + str(students[y]))
            else:
                students[y].append(int(x))
                #y.insert(x)
            
            print(y)
            print(students)
            

        addsSudentGrade()
        #How Do I Add a Value to an array in a dictionary in visual Basic?
        # next create a loop to the bigining of the program here!!!
        
    elif z == 2:
        y = input("Student Name:  ")
        x = eval(input("Please put " + str(y)+ "'s grade in here:  "))
        def deadstudent():
            del students[y]
            print(students)  # creat a function that
        deadstudent()
         #Create a look backt tothe top, a look function that you can call 5 times
        
    elif z == 3:#HERE_____________________________________________________________________________
        import statistics as stat
        for ''' '''  in students:
            l = students[]
            
        y = input("Student Name:  ")
        l = stat.mean(y)
        
        #creat a function that calculates the averafe grade of a student
        print(str(y)+ ", your average grade is" + str(l) + " Good Job!")
        print(students)
    elif z == 4:
    # Close the Program
        close = input(print("Are you sure you want to Close this program? Enter y or n:  "))
        if close == n:
            Main()
        elif close == y:
            print("Have a Nice Day, Bite!!!")
            exit()  
        else:
            main()
            
        
    elif z == 5:
    #Add A Student
        y = str(input("Student Name:  "))
        x = eval(input("Please put " + str(y)+ "'s grade in here:  "))
        def addstudent():
            students[y] = None
            print(students)

        addstudent()
    elif z == 6:
        def whatisgrade():
            y = str(input("Student Name:  "))
            print(students[y])
            # See Specific sudents grades
        whatisgrade()
    else:
        main()
        '''print("A simple program to keep grades and calculate averages for students by treachers.")
        z = 0



    print("Welcone to Grade Central\n [1] - Enter grades \n [2] - Remove students \n [3] - Students Average Grades \n [4] - Exit \n ")
    z = eval(input(print("What Would you like to do Today? (Enter a Integer, 1, 2, 3, or 4  Here):  ")))
        
    # create a loop that circles back to the begining.'''
        
admins = {"python":'pass123@', '123':'456'}
login = input("Username:  ")
passw = input("password:  ")

if login in admin:
    if admins[login] == passw:
    While True:
        main()
         

main()

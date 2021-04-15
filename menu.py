from assignment2 import bodymass
from assignment2 import retirement


while(True):
    print("============================")
    print("Pick one of the following: ")
    print("")
    print("1- Calculate body mass.")
    print("2- Calculate Retirement.")
    print("Press any other key to exit")

    choice = input("::")

    if (choice == "1"):
        pounds = input("type your body mass in pounds: ")
        height= input("type how many feet is your hight: ")
        print("your body mass is: " + str(bodymass(float(pounds), float(height))))
    elif (choice == "2"):
        age = input("your age:: ")
        salay = input("Salary: ")
        percentage = input("Percentage: ")
        goal = input("Saving goal: ")
        print("you are meeting your goal when you become: " + retirement(int(age), float(salay), int(percentage), float(goal)))
    else:
        print("exited")
        break

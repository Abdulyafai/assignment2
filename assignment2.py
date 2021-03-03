
def bodymass(pounds, height):
    if (height <= 0 or height > 8):
        return "Height need to be between 1 and 8"
    elif (pounds <= 0 or pounds > 400):
        return "pounds should be between 1 and 400"

    kg = pounds * 0.453592
    metr = height * 0.3048

    return kg/(metr*metr)

def retirement(age, salary, perc, goal):
    if (age == 0):
        return "Age cannot be 0"
    elif (perc > 100 or perc <= 0):
        return "Percentage should be between 0 and 100"
    elif (age > 100):
        return "You cannot live over 100 years"
    elif (salary <= 0):
        return "Salary cannot be 0 or less"
    else:
        years = goal/(salary * (perc/100))
        x = years + age
        string = "{:0.2f}".format(x)
        if ((x) > 100):
            return ("you will die before you meet your goal, you'll meet your goal when you are (" + string + ") years old")
        else:
            return string



    








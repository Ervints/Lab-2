print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    userInput = str(input())
    splitInput = userInput.split(",")
    floatInput = [float(i) for i in splitInput]
    return floatInput

def calc_average(listOfInput):
    listLength = len(listOfInput)
    total = 0
    for i in range(listLength):
        total = total + listOfInput[i]
    average = total / listLength
    return average

def find_min_max(listOfInput):
    listLength = len(listOfInput)
    min = listOfInput[0]
    max = listOfInput[0]
    for i in range(listLength):
        if listOfInput[i] < min:
            min = listOfInput[i]
    for i in range(listLength):
        if listOfInput[i] > max:
            max = listOfInput[i]
    minMax = [min, max]
    return minMax

def sort_temperature():
    print()

def calc_median_temperature():
    print()

def main():
    display_main_menu()
    userInput = get_user_input()
    average = calc_average(userInput)
    minMax = find_min_max(userInput)
    print("The average is: " +str(average))
    print("The minimum is " +str(minMax[0]) +" and the maximum is " +str(minMax[1]))

if __name__ == "__main__":
    main()
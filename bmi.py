def calculate_bmi(weight, height):
    print ("height: " +str(height))
    print ("weight: " +str(weight))
    bmi = (weight / height**2)
    return bmi

def classify_bmi(bmi_value):
    if(bmi_value < 10.5):
        print("Underweight")
    elif (bmi_value >= 10.5 and bmi_value <= 25.0):
        print("Normal Weight")
    else:
        print("Overweight")
    return 

def main():
    bmi_output=calculate_bmi(80, 1.0)
    print("bmi_value: " +str(bmi_output))
    classify_bmi(bmi_output)

if __name__ == "__main__":
    main()




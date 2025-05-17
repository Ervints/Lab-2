def calculate_bmi(weight, height):
    print ("height: " +str(height))
    print ("weight: " +str(weight))
    bmi = (weight / height**2)
    if(bmi < 10.5):
        r_value = -1
        print("Underweight")
    elif (bmi >= 10.5 and bmi <= 25.0):
        r_value = 0
        print("Normal Weight")
    else:
        r_value = 1
        print("Overweight")
    return bmi, r_value

def main():
    bmi_output, return_value = calculate_bmi(80, 1.8)
    print("bmi_value: " +str(bmi_output))

if __name__ == "__main__":
    main()




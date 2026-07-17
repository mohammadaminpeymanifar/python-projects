weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

BMI = weight / (height ** 2)

if BMI < 18.5 :
    print("You are underweight")
if 24.9 < BMI < 18.5 :
    print("You are normal")
elif BMI > 24.9 :
    print("You are obese")


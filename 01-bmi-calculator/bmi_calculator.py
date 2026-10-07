name=input("Enter your Name\n")
print("Hello " + name)
gender=input("Please specify your gender\n")
age=input("Enter your Age\n")
Height=float(input("Enter your Height (in m)\n"))
Weight=int(input("Enter your Weight (in Kgs)\n"))

BMI=Weight//Height**2
if BMI < 18.5:
    print("Uh-Oh! You are Underweight")
elif BMI < 25:
    print("Yayy! Your BMI is Normal")
elif BMI < 30:
    print("Uh-Oh! You are Overweight")
else:
    print("Oh No! You are Obese")

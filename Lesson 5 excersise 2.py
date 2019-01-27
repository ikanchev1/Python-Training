#weight
W = float(input("Enter your weight in kilograms: ").replace(",","."))
#height
H = float(input("Enter your height in meters: ").replace(",","."))

#body mass index
BMI = W/(H*H)

#print result
bmiIndex = round(BMI,2)

if bmiIndex <= 18.5:
    print("Underweight")
elif bmiIndex > 18.5 and bmiIndex <= 24.9:
    print("Normal")
elif bmiIndex >= 25 and bmiIndex <= 29.9:
    print("Overweight")
elif bmiIndex >= 30:
    print("Obesity")
else:
    print("Something is wrong here.. Check your program :)")

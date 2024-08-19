name = input("enter your name")
education = input("whats your education")
age = input("enter your age")
height = input("enter your height")

age = int(age)
education = int(education)
height = float(height)

if  (age >= 18 and education >= 14) or  (education >=14 and height >= 5) or(age >=18 and height >= 5):
    print("Welcome re, you are eligible for the job.")
else:
    print("Sorry, you are not eligible for the job.")





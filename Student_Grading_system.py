#Inputting student details

name = input("Enter name: ")
Index_id = int(input("Enter Index Number"))

scores = int(input("Enter Score"))

#control flow session

if scores >= 70:
    Grade = "A"
elif scores >= 60:
    Grade = "B"
elif scores >= 50:
    Grade = "C"
elif scores >= 40:
    Grade = "D"
else:
    Grade = "F"

print("You had Grade:", Grade)
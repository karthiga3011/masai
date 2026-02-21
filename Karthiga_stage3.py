name=input("enter name: ")
mark1=float(input("Enter mark for subject 1: "))
mark2=float(input("Enter mark for subject 2: "))
mark3=float(input("Enter mark for subject 3: "))
total=mark1+mark2+mark3
percentage=(total/300)*100
if percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=40:
    grade="C"
else:
    grade="F"
print("Name: ",name)
print("Total: ",total)
print("Percentage: ",percentage)
print("Grade: ",grade)
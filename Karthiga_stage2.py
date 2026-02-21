num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
operator=input("enter operator (add,sub,mul,div): ")
if operator=="add":
    result=num1+num2
    print("Result: ",result)
elif operator == "sub":
    result=num1-num2
    print("Result: ",result)
elif operator== "mul":
    result=num1*num2
    print("Result: ",result)
elif operator=="div":
    if num2==0:
        print("error: division by 0 is not allowed")
    else: 
        result =num1/num2
        print("Result: ",result)
else:
    print("Invalid operator")

if result>0:
    print("Positive")
elif result<0:
    print("Negative")
else:
    print("Zero")
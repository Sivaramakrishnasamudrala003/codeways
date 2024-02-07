oper=input("Enter the operator ")
if(oper=="+" or oper=="-" or oper=="*" or oper=="/"):
    num1=int(input("Enter the first number "))
    num2=int(input("Enter the second number "))
    if(oper=="+"):
        result=num1+num2
    elif(oper=="-"):
        result=num1-num2
    elif(oper=="*"):
        result=num1*num2
    elif(oper=="/"):
        result=(num1/num2)
    print(result)
else:
    print("Please enter an operator")





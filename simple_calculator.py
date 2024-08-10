
def add(a, b): 
    return a + b 
  
def subtract(a, b): 
    return a - b 
  
def multiply(a, b): 
    return a * b 
  
def divide(a, b): 
    if(b==0):
	print("Division by 0 is not possible)
	return 0
    return a / b 


num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

print("Operation: +, -, *, /") 
select = input("Select operations: ")

if select == "+":
    print(num1, "+", num2, "=", add(num1, num2)) 
  
elif select == "-": 
    print(num1, "-", num2, "=", subtract(num1, num2)) 
  
elif select == "*": 
    print(num1, "*", num2, "=", multiply(num1, num2)) 
  
elif select == "/": 
    print(num1, "/", num2, "=", divide(num1, num2)) 

else: 
    print("Invalid input")
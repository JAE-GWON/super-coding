#함수 정의하기기
def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 // num2

num1 = int(input())
num2 = int(input())
operation = input()
if operation == "+":
    print(plus(num1, num2))
elif operation == "-":
    print(minus(num1, num2))
elif operation == "*":
    print(multiply(num1, num2))
elif operation == "//":
    print(divide(num1, num2))
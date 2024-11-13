n = int(input("Enter a number :"))

def findFactorial(num):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * findFactorial(num-1)

factorial = findFactorial(n)
print(factorial)



















number = int(input("enter a positive number :"))
def determine(n):
    if n <= 0 :
        return "Provide a positive number"
    elif n % 2 == 0:
        return "this is even number."
    else:
        return "this is odd number."

result = determine(number)
print(result)









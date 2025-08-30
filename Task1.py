n=input("Enter a number: ")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("Factorial of", n, "is:", result)

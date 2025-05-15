n=5
def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
print("enter a number", n)
factorial(n)
print('factorial of',n,'is',factorial(n))




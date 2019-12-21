# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n!=1×2×...×n
# For the given integer n calculate the value n!. Don't use math module in this exercise.

n = int(input("Enter number:"))
result = 1
if n < 0:
    print("Factorial doesn't exist")
elif n == 0:
    print(1)
else:
    for i in range(n, 0, -1):
        result = result * i
    print("Factorial is", result)

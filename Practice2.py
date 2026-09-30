num = int(input("Enter Number to find factorial of First Numbers\n"))

factorial = 1

for val in range(num, 0, -1):

    factorial *= val

print("Factorial of First ",num," = ", factorial)
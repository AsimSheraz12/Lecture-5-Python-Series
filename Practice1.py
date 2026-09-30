num = int(input("Enter Number to find Sum of First Numbers\n"))
sum = 0

for val in range(0, num+1):
    sum += val

print("Sum of First ",num," = ", sum)


# Same Question done using while

sum = 0

i = 0

while i <= num:
    sum+=i
    i+=1

print(sum)
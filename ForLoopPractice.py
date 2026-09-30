# Print List Elements using For loop

Nums = []

i = 0

while i < 10:
    Nums.append((i+1)**2)
    i+=1


for val in Nums:
    print("Value is : ", val)


searchNUmber = int(input("\nEnter Number for Search\n\n"))

for value in Nums:
    if value == searchNUmber :
        print("Number Found")
        break
else:
    print("Not Found")
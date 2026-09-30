#Print Numbers from 1 to 100

a = 1

while a<= 100:
    print(a)
    a+=1

print("\n\n\n\n\n")

#Reverse Counting 100 to 1

b = 100

while b>= 1:
    print(b)
    b-=1


#Multiplication of Number 1

c =  int(input("Enter the Number for Print table 1 to 10 \n"))

d = 1

print("\n\n")

while d<=10:
    print(f"{c} X {d} = {c*d}")
    d+=1

e = 1

print("\n\n")


while e<=10:
    print(f"{e} element is {e**2}")
    e+=1

numbers = (1 , 4, 9, 16, 25, 36, 49, 64, 81, 100)
search_number = int(input("\nEnter Number for search in Tuple\n"))

g = 0

while g < len(numbers):
    if numbers[g] == search_number:
        print("Number Found")
        break

    g += 1
else:
    print("Number not Found")
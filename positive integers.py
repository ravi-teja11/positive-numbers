# Program to Find the Positive Integers in Lists

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print("List1=", list1)
print("List2=", list2)
print("\nPositive NUmbers in List1 =")
for number in list1:
    if number > 0:
        print(number, end=",")
print("\nPositive Numbers in List2 =")
for number in list2:
    if number > 0:
        print(number, end=",")
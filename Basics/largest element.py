# Example: [10, 5, 20, 8, 15] → 20

num = int(input("Enter the number of elements in the list: "))
numbers = []

for i in range(num):
    elements = int(input("Enter element {}: ".format(i + 1)))
    numbers.append(elements)

print("The largest element in the list is:", numbers)

highest = numbers[0]
second_highest = numbers[0] 
for num in numbers:
    if num > highest:
        second_highest = highest
        highest = num
    elif num > second_highest and num != highest: # 2nd largest means if number is greater than second_highest and not equal to highest
        second_highest = num
            
print("The largest element in the list is:", highest)
print("The second largest element in the list is:", second_highest)
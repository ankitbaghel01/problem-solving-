num = int(input("Enter the number of elements in the list: "))

numbers = []

for i in range(num):
    elements = int(input("enter element {}:".format(i + 1)))
    numbers.append(elements)
    
print("numbers value ", numbers)

# way 1 

reverse = numbers[::-1]

print("Reversed list is:", reverse)

# way 2

reverse_array = []

for i in range(len(numbers)-1,-1,-1):
    reverse_array.append(numbers[i])
    
print("Reversed list is:", reverse_array)
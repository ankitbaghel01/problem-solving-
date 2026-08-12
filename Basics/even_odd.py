num = int(input("Enter the number of elements in the list: "))

numbers = []

for i in range(num):
    elements = int(input("enter element {}:".format(i + 1)))
    numbers.append(elements)
    
print("numbers value ", numbers)


# way 1 

even = list(filter(lambda x: x % 2 == 0, numbers))    
odd = list(filter(lambda x: x % 2 != 0, numbers))


# way 2 

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        
        
print("Even numbers in the list are:", even_numbers, "and the time complexity is O(n)")        
print("Odd numbers in the list are:", odd_numbers, "and the time complexity is O(n)")        
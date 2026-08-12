num = int(input("Enter the number of elements in the list: "))

numbers = []

for i in range(num):
    elements = int(input("enter element {}:".format(i + 1)))
    numbers.append(elements)
    
print("numbers value ", numbers)

def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

print("Is the list sorted?", is_sorted(numbers))
num = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(num):
    elements = int(input("enter element {}: ".format(i + 1)))
    numbers.append(elements)
    
print("numbers value ", numbers)


def sum_all_elements(numbers):
    total = 0 
    for num in numbers:
        total += num
    return total


def sum_all_elements_recursive(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] +sum_all_elements_recursive(numbers[1:])
    

def sum_using_reduce(numbers):
    from functools import reduce
    return reduce(lambda x, y: x + y, numbers)


sum = sum_all_elements(numbers)
sum_recursive = sum_all_elements_recursive(numbers)
sum_reduce = sum_using_reduce(numbers)      

print("Sum using iteration:", sum ,"and the time complexity is O(n)")
print("Sum using recursion:", sum_recursive, "and the time complexity is O(n)")
print("Sum using reduce:", sum_reduce, "and the time complexity is O(n)")

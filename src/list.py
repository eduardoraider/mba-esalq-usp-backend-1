numbers = [1, 2, 3, 4, 5]

print("List of numbers:", numbers)

print("First element:", numbers[0])  # First element
print("Last element:", numbers[-1])  # Last element

numbers.append(6)
print("List after adding 6:", numbers)

numbers.remove(3)
print("List after removing number 3:", numbers)

print("Elements of the list:")
for number in numbers:
    print(number)

if 2 in numbers:
    print("The number 2 is in the list.")
else:
    print("The number 2 is not in the list.")

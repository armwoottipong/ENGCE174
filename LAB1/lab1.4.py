numbers = [1, 2, 3, 4, 5]
           
print("First element : ", numbers[0])
print("Last element :", numbers[-1])

print("Sliced elements : ", numbers[2:4])

numbers.append(6)
print("After append : ", numbers)


numbers.remove(3)
print("After removal : ", numbers)
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

# Expected Output :

# Number of even numbers : 4

# Number of odd numbers : 5
# check the given expected output by using this program
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring tuples
odd = 0
even = 0
for i in numbers:
    if  i % 2:
        odd+=1
    else:
        even+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
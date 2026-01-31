# Question 3

#function created to compute x^y(x to the power of y)
def powerCalculation(x, y):
    return x ** y

#example input given to us in the assignment
exampleInput = [[5, 2], [3, -1], [4, 3], [2, 0]]
results = []

#for loop
for x, y in exampleInput:
    # Skip any negative exponent
    if y < 0:
        continue

    # Calculate and store the valid results
    value = powerCalculation(x, y)
    results.append(value)

# Print all the valid results
print(results)
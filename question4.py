#Question 4

#Starter code for question 4
from random import random

values = [random() for i in range(20)]
x = random()

#my logic

#sorted list of values
sortedList = sorted(values)

#all indices where value is greater than or equal to x
matchingIndices = []

for index in range(len(sortedList)):
    if sortedList[index] >= x:
        matchingIndices.append(index)

#print the outputs
print("Sorted list:", sortedList)
print("Value of x:", x)

if len(matchingIndices) > 0:
    print("First matching index:", matchingIndices[0])
else:
    print("No values are greater than or equal to x")
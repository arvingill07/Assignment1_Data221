#Question 6

#creating function
def distributionAnalysis(numbers):
    distributionDictionary = {}

    totalCount = len(numbers)

    #find unique values
    uniqueValues = []
    for value in numbers:
        if value not in uniqueValues:
            uniqueValues.append(value)

    #sort the unique values
    uniqueValues.sort()

    #calculate percentage of elements in the list that are less than/ equal to key
    for number in uniqueValues:
        countEqualOrLess = 0

        for value in numbers:
            if value <= number:
                countEqualOrLess += 1

        percentage = (countEqualOrLess / totalCount) * 100
        distributionDictionary[number] = percentage

    return distributionDictionary

#given list from assignment
numbers = [3, 1, 2, 3, 4, 2]

#print the final results
print(distributionAnalysis(numbers))






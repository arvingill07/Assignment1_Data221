#Question 2 Assignment 1

#creating a reusable function for the question
def stringDictionary(listOfStrings):
    result = {}

    for word in listOfStrings:
        wordLength = len(word)

        # Check if the length is even or odd
        if wordLength % 2 == 0:
            parity = "even"
        else:
            parity = "odd"

        # Store information in the dictionary
        result[word] = {
            "length": wordLength,
            "parity": parity
        }

    return result

#expected result for question
#this can be turned into a more usable function if we turn "expected_result" into an input statement
expected_result = stringDictionary(["data", "science"])

#printing final result
print("{")
for key in expected_result:
    print(f' "{key}": {expected_result[key]},')
print("}")
#Question 1 Assignment 1


#example structure for question 1
threshold = 100
product = 1
currentNumber = 1

#my own loop
while product <= threshold:
    currentNumber = currentNumber + 1
    product = product * currentNumber

#loop finished printing results
print(f"Finished product: {product}")
print(f"Integer that caused exceeding of threshold: {currentNumber}")
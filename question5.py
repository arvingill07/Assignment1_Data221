import math
#Question 6

#function to calculate areas
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if type(radiusOfCircle1) != int or type(radiusOfCircle2) != int:
        return "You've given an invalid value, please enter an integer value"
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "You've given an invalid value, please enter a positive value"

    areaOfCircle1 = math.pi * (radiusOfCircle1**2)
    areaOfCircle2 = math.pi * (radiusOfCircle2**2)

    if areaOfCircle1 > areaOfCircle2:
        largerArea = areaOfCircle1
        smallerArea = areaOfCircle2
    else:
        largerArea = areaOfCircle2
        smallerArea = areaOfCircle1

    return (smallerArea/ largerArea) * 100

print(circleAreaCoverage(6, 7))



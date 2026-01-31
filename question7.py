#Question 7

#create function
def convertTime(secondsFromMidnight):
    if secondsFromMidnight < 0 or secondsFromMidnight > 86399:
        return "Invalid input please input a valid time"

    #converting the time
    hours = secondsFromMidnight // 3600
    minutes = (secondsFromMidnight % 3600) // 60
    secs = secondsFromMidnight % 60

    #find out if it's am or pm
    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    hours = hours % 12
    if hours == 0:
        hours = 12

    return str(hours) + " " + str(minutes) + " " + str(secs) + " " + period

print(convertTime(19204))
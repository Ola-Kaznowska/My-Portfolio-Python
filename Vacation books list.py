from math import floor


numberOfPages = int(input("Number of pages: "))
pagesPerHours = int(input("Hours: "))
numberOfDays = int(input("Days: "))

numberOfHours = numberOfPages // pagesPerHours

print(numberOfHours)

hoursToReadPerDay = numberOfHours // numberOfDays
print(hoursToReadPerDay)
number = input("Enter a number: ")

# inputs always gets a string, not integer
print "The number plus 10 is:", int(number) + 10

# {} will be interpreted into an formatable variable
print "The number in format is {0:.2f}".format(number)

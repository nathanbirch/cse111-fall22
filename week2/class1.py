import math
import random
from datetime import datetime
###########################################################################
############################## challenge day ##############################
###########################################################################
###### class challenge #1 ######
    # See how many of the following functions you can call in a single line of code
        # input, print, open, len, range, int, float, type, str, abs, round, list, set, dict
    # Find at least two other built-in functions that you can call in a single line of code


###### class challenge #2 ######
    # execute the print() function using 5 different arguments (not of the same type)


###### class challenge #3 ######
    # import the math package and compute: 
        # 17 to the power of 9 
        # divide by 3
        # round up to the nearest integer
        # subtract 6
        # return a boolean value that indicates whether the result is even (True) or odd (False). 


###### class challenge #4 ######
    # import the random package and make a list of random numbers...sort it from smallest to largest


###### class challenge #5 ######
    # if it is an even minute (computer clock)
    # print "even minute"
    # otherwise print "odd minute"



############################# Class Solutions #############################
# Challenge #1
print("\n*** Challenge #1 ***\n", str(int(float(input("Enter a number: ")))))
print("\n*** Challenge #1 ***\n", str(round(float(input("Enter a number: ")), 1)))
print("\n*** Challenge #1 ***\n", type(len(list((round(math.sqrt(abs(float(str(int(input("Enter an integer: "))))))), 1)))))

# Challenge #2
print("\n*** Challenge #2 ***\n", "Hello, I", 20, sep=" am ", end = " how old are you?", flush=True)
print("\n*** Challenge #2 ***\n", "hello", "world", "hello", "world", sep="\n")

# Challenge #3
def random_math():
    return (math.ceil(math.pow(17, 9) / 3) - 6) % 2 == 0
print("\n*** Challenge #3 ***\n", random_math())

# Challenge #4
random_number_list = []
while len(random_number_list) < 100:
    random_number_list.append(random.randint(0, 1000))
random_number_list.sort() # sort(reverse=True)
print("\n*** Challenge #4 ***\n", random_number_list)

# Challenge #5
now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"
print("\n*** Challenge #5 ***\n", display_message)

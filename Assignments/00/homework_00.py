"""in this homework, type all your answers as string variables that get printed out, so that your TA can run the
    program and see all of your answers.
"""

'''
    00. what are the difference between variables, statements, and expressions in python? (3 POINTS)
'''
# type your answer here
a1 = "00. \n\t- Variables store values in memory.\n\t- Expressions evaluate to values.\n\t- Statements declare and hold executable commands/functions."
print(a1 + "\n")

'''
    01. what is the difference between a string, an integer, and a float variable in python?
        what is a situation where if you thought something was a float, and instead it was an int, you might get in 
        trouble? What is a situation where if you thought somethinng was a int, and instead it was a string, you
        might get in trouble? (3 POINTS)
'''
print("01. A String represents an array of characters, an integer is a number with no decimals, a float variable is a variable that a decimal.\
 There is no common situation in Python 3 that would result in an issue with confusing ints as floats because division is not automatically floored. If you are\
 working a string you believe to be an int you can run into errors when using operands or functions that are imcompatible with integers. \n")

'''
    02. what is the difference between an operator and an operand? What is the difference between the following kind
    of operators (3 POINTS):
    - Arithmetic Operators
    - Comparison (Relational) Operators
    - Assignment Operators
    - Logical Operators
    - Identity Operators
'''
print("02. Operators are characters that represent different forms of computation and operands are the values the operators work upon.\n" \
    + "\t- Arithmetic Operators perform basic mathmatical operations with numerical values\n"\
    + "\t- Comparison Operators compare two values and result in a boolean\n" \
    + "\t- Assignment Operators assign values to variable\n" \
    + "\t- Logical Operators are used to combine conditional statements\n" \
    + "\t- Identity Operators check if an object is the same object (by memory location)\n")


'''
    03. Describe the difference behavior between the two following lines of code (1 POINT):
      if not (x > 02) or (y > 02):
      if not ((x > 02) or (y > 02)):  
'''
print("03. The first line's if statement conditional is True when x is less than or equal 2 or when y is greater than 2.\
 The second line of code's condition is True when either x is less than or equal to 2 and y is less than or equal to 2\n")

''' 
    05. Write a program that asks for a temperature in celcius and converts it to farenheit, and prints it out. 
    (3 POINTS)
'''
print("04. Celcius Converter\n---------------------\n")
tempEntered = False
while(not tempEntered):
    try:
        c = input("Enter the temperature in Celcius: ")
        print("{} Celcius is {} Farenheit\n".format(c, int(c) * 9/5 + 32))
        tempEntered = True
    except ValueError:
        print("(!) ERROR: Enter a number")

''' 
   06. write a program that asks you to type in the score of five exams, one at a time, and calculates and
        prints the mean score, the highest score, the lowest score, and the average score dropping the lowest score. 
        The output should look this this: (7 POINTS)
        
        Mean Score: 89.5343
        Lowest Score: 70
        Highest Score: 100
        Mean After Dropping Lowest: 92.412
'''
print("06. SCORES STATISTICS\n---------------------")
scores = [0,0,0,0,0]

i = 0

while i < len(scores):
    try:
        scores[i] = int(input("Enter the score #{}: ".format(i + 1)))
        i += 1
    except ValueError:
        print("(!) ERROR: Enter a number")

sum = 0
for x in scores:
    sum += x

min = min(scores)
max = max(scores)
mean = sum/len(scores)

scores.remove(min)

sum = 0
for x in scores:
    sum += x
madl = sum/len(scores)

print("\nMean Score: {}".format(mean) \
    + "\nLowest Score: {}".format(min) \
    + "\nHighest Score: {}".format(max) \
    + "\nMean After Dropping Lowest: {}".format(madl))
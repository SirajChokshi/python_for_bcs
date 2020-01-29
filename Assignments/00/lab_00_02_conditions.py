X = 1
Y = 2
Z = 10

A = '00'
B = '01'
C = '10'
D = 'dog'

if X == D:
    print("Same")
else:
    print("Different")

if X > Y:
    print(X)
else:
    print(Y)

'''
    change the above code to compare:
        Y & Z --> Z
        X & Z --> Z
        A & B --> B
        A & C --> C
        B & C --> C
        C & D --> D
        Z & C --> TypeError
'''

# what will this "AND" code do?
if (X > Z) and (int(A) == X):
    print("Success")
else:
    print("Fail")
# print "Fail"

# what about this "OR" code?
if (X > Z) or (int(A) == X):
    print("Success")
else:
    print("Fail")
# print "Fail"

# is this is the same as the AND code or the OR code?
if X > Z:
    if int(A) == X:
        print("Success")
    else:
        print("Fail")
else:
    print("Fail")

# the AND code

# how would you change it to make it behave like the other one
# in other words, if the code above is like the AND code, change it to behave like the OR code
# but continuing to use two separate if statements instead of one combined one
# 
# FIXED CODE:
if X > Z:
    print("Success")
elif int(A) == X:
    print("Success")
else:
    print("Fail")

# FIXED w/ TWO if STATEMENTS
if X > Z:
    print("Success")
else:
    if int(A) == X:
        print("Success")
    else: 
        print("Fail")
"""Homework 1
"""
'''
    1. what is the difference between a list and a tuple? What is a situation you might want to use a tuple instead
    of a list? (1 POINTS)
'''
a1 = "A list is mutable (editable) while a tuple is not. You would want to use a tuple instead\
      of a list when you have a set of static data that you do not want to be modifyable."
print(a1 + "\n\n")

'''
    2. the for loop lab described two ways of writing for loops. How were they different? What are the advantages
    of each way of doing it? (1 POINTS)
'''
a2 = "One way of writing loops defines a range in which an index can be used which is useful when one needs to\
  keep track of how far through the are in a list. The other way uses a reference to an item in the list which\
  can be helpful when one is just trying to access the item itself and does not need to keep track of an index"
print(a2 + "\n\n")

'''
    3. what do "break" and "continue" do in loops? (1 POINTS)
'''
a3 = "'break' exits a loop while the loop is progress and 'continue' restarts a loop from the beginning of its contents"
print(a3 + "\n\n")

'''
    3. what is a list "slice"? How do you slice a list, and what is the result? (1 POINTS)
'''
a4 = "a slice is a segment of a list defined by entered parameters. The result is a subset of the list"
print(a4 + "\n\n")


'''
5. there are a bunch of useful things you can do with lists. write code that prints out the result after doing the 
following things to the lists below: 
of the lists below: (5 POINTS)
    a) sort them
    b) get their sizes
    c) concatenate them
    d) get the count of a particular item in a list
    e) remove the duplicates from a list
'''
list_a = [1, 2, 3, 4, 5, 6]
list_b = ["dog", "cat", "lion", "tiger", "rat", "mouse", "rat", "mouse"]
list_a.sort()
list_b.sort()
print(list_a)
print(list_b)
list_c = list_a + list_b
print("list_a is {} entries long and list_b is {} entries long".format(len(list_a), len(list_b)))
print(list_c)
print("'rat' appears {} times in list_b".format(list_b.count("rat")))
list_b.remove("rat")
print(list_b)

'''
5. A string can be treated like a list. Write code that that uses the input function to take in a string, and
save it to a variable. Then write a for loop that prints out each letter in the string, one by one. (2 POINTS)
'''
string = input("Enter a string: ")
for letter in string:
  print(letter)


'''
6. You can make a list out of anything, even other lists. Write code that takes in input from the keyboard, and adds
each word to a list. If the list is three items long, add that list as an element to a "master_list". For example, 
if the words "one" through "nine" were typed at the keyboard, the resulting "master_list" should be:
master_list = [["one", "two", "three"], ["four", "five", "six"], ["seven", "eight", "nine"]]
(3 POINTS)
'''
master_list = []

txt = input("Enter a list:")

tmp_list = txt.split(" ")

sum = 0
tmp = []
for val in tmp_list:
  if sum % 3 == 0:
    master_list.append(tmp)
    tmp = []
  sum += 1
  tmp.append(val)
master_list.pop(0)

print(master_list)

'''
7. you can use the split() function on a string. The result is a list, as shown below. write code that:
    - creates a second list called "type_list" that has all duplicates from first list removed
    - print out the type_lst
    - has a for loop that iterates over each item in "type_list", prints out that word, and prints out how many times it 
      occurs in "token_list", the result should look something like:
      i: 2
      am: 2
      the: 3
      egg: 2
      man: 1
      ...
(3 POINTS)
'''
input_string = "i am the egg man. they are the egg men. i am the walrus. goo goo g'joob."
token_list = input_string.split(" ")
print(token_list)

type_list = []

for val in token_list:
  if val not in type_list:
    type_list.append(val)

print(type_list)

for val in type_list:
  print("{}: {}".format(val, token_list.count(val)))



'''
8. Correctly complete the code for lab_01_05_big5e.py. Paste the code here.
(4 POINTS)
'''

print("\n")


questions = ["I am the life of the party", "I don't talk a lot", "I feel comfortable around other people",\
 "I keep in the background", "I start conversations", "I have little to say", "I talk to a lot of different people at parties",\
  "I do not like to draw attention to myself", "I do not mind being the center of attention", "I am quiet around strangers"]

answers = []

i = 0
final_score = 20

print("This is the Big Five Personality Test\n\
    It will help you understand why you act the way that you do and how your personality is structured.\n\
    For each statement 00-50 mark how much you agree with on the scale 00-05, where:\n\
    01=disagree\n\
    02=slightly disagree\n\
    03=neutral\n\
    04=slightly agree\n\
    05=agree\n\
    1. I am the life of the party.\n\
    2. I don't talk a lot.\n\
    3. I feel comfortable around other people.\n\
    4. I keep in the background.\n\
    5. I start conversations.\n\
    6. I have little to say.\n\
    7. I talk to a lot of different people at parties.\n\
    8. I do not like to draw attention to myself.\n\
    9. I do not mind being the center of attention.\n\
    10. I am quiet around strangers.\n")

while i < len(questions):
  try:
    val = int(input("Question {}) {}:\n".format(i + 1, questions[i])))
    if val > 5 or val < 1:
      raise ValueError
    elif i % 2 != 0:
      answers.append(-val + 1)
      i += 1
    else:
      answers.append(val - 1)
      i += 1
  except ValueError:
    print("(!) ERROR: Enter a numerical value between 1 and 5")
for r in answers:
  final_score += r

print("\nYour Entroversion Score is: {}!\n".format(final_score))
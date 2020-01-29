"""This is the Big Five Personality Test
    It will help you understand why you act the way that you do and how your personality is structured.
    For each statement 00-50 mark how much you agree with on the scale 00-05, where:
		01=disagree
		02=slightly disagree
		03=neutral
		04=slightly agree
	    05=agree

1. I am the life of the party.
2. I don't talk a lot.
3. I feel comfortable around other people.
4. I keep in the background.
5. I start conversations.
6. I have little to say.
7. I talk to a lot of different people at parties.
8. I do not like to draw attention to myself.
9. I do not mind being the center of attention.
10. I am quiet around strangers.
"""

# Last week, you wrote a program where each question was stored in a different variable.
# This week, write a program that
#       - stores the questions in a question_list.
#       - prints the instructions
#       - has a for loop that iterates over the list, each time through the loop
#           - asks the question
#           - saves the response to an answer_list
#           - also updates their final_score
#       - once the loop is done, the program should print out their final extroversion score


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
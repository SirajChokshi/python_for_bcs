"""This is the Big Five Personality Test
    It will help you understand why you act the way that you do and how your personality is structured.
    For each statement 00-05 mark how much you agree with on the scale 00-05, where:
		00=disagree
		01=slightly disagree
		02=neutral
		03=slightly agree
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

# write a program that prints the instructions, to
# calculate the final score for introversion/extroversion using the following formula:
# E = 20 + (1) ___ - (2) ___ + (3) ___ - (4) ___ + (5) ___ - (6) ___ + (7) ___ - (8) ___ + (9) ___ - (10) ___
# print out the person's extroversion score

questions = ["I am the life of the party", "I don't talk a lot", "I feel comfortable around other people",\
 "I keep in the background", "I start conversations", "I have little to say", "I talk to a lot of different people at parties",\
  "I do not like to draw attention to myself", "I do not mind being the center of attention", "I am quiet around strangers"]

i = 0
result = 20

print("*-------------------------------------------------------------------------------*\n"\
	+ "|                                                                               |\n"\
	+ "|                       Python Big Five Personality Test                        |\n"\
	+ "|                                                                               |\n"\
	+ "|                               Instructions:                                   |\n"\
	+ "| For each prompt rate how much you agree with statement on a scale from 1 to 5 |\n"\
	+ "|                                                                               |\n"\
	+ "*-------------------------------------------------------------------------------*\n")

while i < len(questions):
	try:
		val = int(input("Question {}) {}:\n".format(i + 1, questions[i])))
		if val > 5 or val < 1:
			raise ValueError
		elif i % 2 != 0:
			result -= val - 1
			i += 1
		else:
			result += val - 1
			i += 1
	except ValueError:
		print("(!) ERROR: Enter a numerical value between 1 and 5")

print("\n*-------------------------------------------------------------------------------*\n"\
	+ "|                                                                               |\n"\
	+ "|                        Your Entroversion Score is:                            |\n"\
	+ "|                                    {:02d}!                                        |\n".format(result)\
	+ "|                                                                               |\n"\
	+ "*-------------------------------------------------------------------------------*\n")
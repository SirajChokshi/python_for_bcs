'''
    we are finally ready to write a program that does the entire big 5 personality survey!
    look at the file big5_questions.csv. You will see it has four columns.
        - question number
        - scale (Openness, Conscientiousness, Extroversion, Agreeableness, Neuroticism)
        - question
        - scoring value

    - read in the data from the file, and store the values in a list of tuples like shown below.
    big5_questions_list = [(1, "E", "I am the life of the party.", 1),
                           (2, "A", "I feel little concern for others.", -1),
                            ...]
    - create a score_list, with the following initial scores for the OCEAN variables: [20, 20, 8, 5, 11]
    - print the instructions (get them from last week
    - loop through the list of questions. for each question:
        - print the question
        - use a while loop to ensure that the user enters a valid response (a number 1-5)
        - when a valid answer is given, add or subtract that value (based on the question's scoring value)
            to the appropriate OCEAN score in the score list
        - when all questions are complete, print the five final scores using this format
            you answered N questions. your scores were:
            openness     conscientiousness     extroversion     agreeableness     neuroticism
            20           20                    8                5                 11
        - the value of N should be the number of questions that were answered
        - there should be five spaces between each scale label, and the scores should be left-aligned under the label
        - create yourself an "escape hatch" answer "DONE". if "DONE" is typed as the answer to a question, the you
            should break out of the question answering loop and move immediately to printing the scores
            this way, you wont need to type in all 50 answers every time while you test the program
'''

print("This is the Big Five Personality Test\n\
        It will help you understand why you act the way that you do and how your personality is structured.\n\
        For each statement 00-50 mark how much you agree with on the scale 00-05, where:\n\
        01=disagree\n\
        02=slightly disagree\n\
        03=neutral\n\
        04=slightly agree\n\
        05=agree\n")

score_list = [20, 20, 8, 5, 11]

questions = []

f = open('big5_questions.csv')
for q in f:
    q = q.split(',')
    questions.append(q)
end = False
for q in questions:
    answering = True
    while answering:
        answer = input("#{}) {}\n".format(q[0], q[2]))
        if str(answer) == 'DONE':
            answering = False
            end = True
            break
        else:
            try:
                val = int(answer)
                if  val > 5 or val < 1:
                    raise ValueError
                else:
                    answering = False
                    x = val * int(q[3])
                    if q[1] == 'O':
                        score_list[0] += x
                    elif q[1] == 'C':
                        score_list[1] += x
                    elif q[1] == 'E':
                        score_list[2] += x
                    elif q[1] == 'A':
                        score_list[3] += x
                    elif q[1] == 'N':
                        score_list[4] += x
            except ValueError:
                print("(!) ERROR: Enter a numerical value between 1 and 5")
                continue
    if end:
        break
print("\n{}     {}     {}     {}     {}".format("openness", "conscientiousness", "extroversion", "agreeableness", "neuroticism"))
final_list = []
for score in score_list:
    final_list.append(str(score))
print("{:8s}     {:17s}     {:12s}     {:13s}     {:11s}\n".format(final_list[0], final_list[1], final_list[2], final_list[3], final_list[4]))

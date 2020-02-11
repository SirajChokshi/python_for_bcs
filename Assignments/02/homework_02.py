import pickle

'''
    1. what happens if you try to open a file that is already open?
    (1 POINT)
''' 
answer1 = "The file is opened again and appears empty using the second reference"
print("\nanswer to question 1: {}\n".format(answer1))


''' 
    2. how do you only read the first 10 characters of a file? type your answer as working python code in the space
        indicated below.
        (1 POINT) 
'''
file = open("test_file1.txt")
answer2 = file.read(10)
print("answer to question 2: {}\n".format(answer2))
file.close()


''' 
    3. What is an "iterator" in python?
    (1 POINT) 
'''
answer3 = "An object containing a countable number of values and allows traversal through values in a list, set or tuple"
print("answer to question 3: {}\n".format(answer3))


''' 
    4. If you want to print out a variable in a string using a .format() statement, so that it takes up 20
    spaces and is right aligned, how do you do that? Change the print statement below appropriately.
    (1 POINT) 
'''

print("answer4\n".rjust(20))


''' 
    5. By default, a print statement prints whatever you tell it to, and also a new line \n. How do you force it to
    not print the new line if you dont want it to. In other words, if you printed three words in three different 
    print statements, they would all end up on the same line instead of on their own lines.
    (1 POINT) 
'''
answer5 = "print them within the same print statement (ex. print(item1, item2, item3)\n or change the end parameter to an empty string (ex. print('test', end='')"
print("answer to question 5: {}\n".format(answer5))


''' 
    6. What is a "pickle" file in python? What are the advantages and disadvantages of pickle files compared to
    regular data files?
    (1 POINT) 
'''
answer6 = "pickle files are encoded string representations of different python iterables. \nPickle files are not readable to people, but it are readable by python and quick to use."
print("answer to question 6: {}\n".format(answer6))


''' 
    7. Create three variables. save them to a pickle file called "my_variables". Load them back in and print them out.
    (2 POINTS) 
'''
# code for #7 here
x = "item1"
y = "item2"
z = "item3"
temp_list = [x, y, z]
pickle.dump( temp_list, open( "my_variables.p", "wb" ) )
output_list = pickle.load(open( "my_variables.p", "rb" ))
print(output_list)
print()


'''
    8.  write code that reads in file 'test_file2.txt', creates a separate file for each geographic region 
        the animals are from, and prints only the animals from that region to the file, one animal per line.
        for example, you should create the file 'africa.txt', and that file should have:
        
        elephant
        lion
        giraffe
        zebra
        hyena
        
        also, the program cannot "hard code" the names of the files. You need to figure out the names of the output 
        files from the input files. For example, if I test your code on a new input file that has animals from china, or
        antarctica, or Wonderland, the program should still work!
        (4 POINTS)
'''
your code for #8 goes here
filename = 'test_file2.txt'
f = open(filename)
data_list = []
for line in f:
    data = line.strip('\n')
    data = data.split(',')
    data_list.append(data)
for data in data_list:
    try:
        f2 = open("{}.txt".format(data[1]), "x")
    except:
        f2 = open("{}.txt".format(data[1]), "a")
    f2.write("{}\n".format(data[0]))
f.close()
f2.close()
print()

'''
    9. write code that:
        0.) takes 'test_file1.txt' as input
        1.) stores each line in list
        2.) uses a for loop to iterate over that list
        3.) uses a second for loop to iterate over each word in each sentence
        5.) uses a while loop to iterate over each letter in the word, until there are no more letters in the word
        6.) prints out the document, one letter at a time, with each word on a different line and each letter separated
                by a space. For example, the first three lines should be:
                
                T h e
                g r i z z l y
                b e a r
        (4 POINTS)
'''
print("Output of question #9")
# your code for #9 goes here
print()
f = open('test_file1.txt')
line_list = []
for line in f:
    line_list.append(line.split(' '))
for line in line_list:
    for word in line:
        string = ''
        count = 0
        while count < len(word):
            string += "{} ".format(word[count])
            count += 1
        print(string)
f.close()
print()

'''
10. Correctly complete this week's Big 5 Personality Test program. Dont type the code here, we will grade it from the 
other file. (4 POINTS)
'''

print("\n\nThis is the Big Five Personality Test\n\
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
f.close()
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

'''
    you can think of python programs as falling into two categories:
    1) short simple "scripts" that are designed to quickly accomplish some task
    2) longer "programs" that are doing a lot of complex things. If you are writing programs, it is important to keep
        them organized for all kinds of reasons.
        - they are easier to read
        - they are easier to debug
        - they are easier to share and work on collaboratively
        - they are easier to remember what the hell you were doing when you pick up a script later
        - most importantly, functions that are well defined, meaning they do one and only one thing, make it really
            easy for you to take a function you made in some earlier program and stick them in a new one, saving you
            lots of time


    big programs are usually organized in the following way:
    a "main" function, that calls a bunch of other functions.
    edit the code below that counts the words in a string that you typed
'''

# def get_input(??????):  # an input argument goes here
     # create a line that gets an input string
     # create a line that returns the input string back to the main function
     
def get_input():
    val = input("Enter your string: ")
    return val

# def get_unique_word_list(???????): # an input argument goes here
     # add the code that creates a list of the unique words in the string
     # return the new list back to the main function

def get_unique_word_list(str):
    word_list = str.split(' ')
    unique_list = []
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list

# def count_words(???????): # input arguments
     # add the code that counts how many times each unique word occurs in the input string, adding those values to a list
     # return this list back to the main program
     
def count_words(str, unique_list):
    word_list = str.split(' ')
    counts = []
    for word in unique_list:
        count = 0
        for otherWord in word_list:
            if word == otherWord:
                count += 1
        counts.append(count)
    return counts

# def print_results(??????): # input arguments
     # add code that prints out each word and each frequency, on its own line, like this:
     # dog: 2
     # cat: 1
     # shoe: 2
     
def print_results(unique_list, word_counts):
    for i in range(len(word_counts)):
        print("{}: {}".format(unique_list[i], word_counts[i]))

# def main():
#     get_input() # edit so it passes and receives appropriate variables
#     get_unique_word_list() # edit so it passes and receives appropriate variables
#     count_words() # edit so it passes and receives appropriate variables
#     print_results() # edit so it passes and receives appropriate variables
#
def main():
    input_str = get_input()
    unique_list = get_unique_word_list(input_str)
    word_counts = count_words(input_str, unique_list)
    print_results(unique_list, word_counts)

main()
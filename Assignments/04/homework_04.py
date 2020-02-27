
def q1():
    # What is the difference between a list, a set, and a dictionary. What is a situation where you would want to use
    # each one?
    your_answer = "A list is an ordered collection of items with repeating values, could be used for keeping track of all the words in a text. A set is an unordered collection with no repeating values, could be used to track progress using a set of numbers with no duplicate values. And a dictionary is a collection where every value has a key mapped to it. A dictionary would be useful when you need to access information by a different name"
    print("Question 1")
    print(your_answer)


def q2():
    # What is a "mutable" object in python, and how is it different from an immutable object? In addition to sets,
    # give an example of a data structure that can be mutable, and one that can be immutable? Sets can be either one.
    # why might you want to make it mutable or immutable?
    your_answer = "A mutable item in python is one that can be changed after it is initialized whereas an immutable object cannot be altered after declaration. Lists can be mutable and tuples are immutable. If a set is being used as a reference you wouldn't want it to be mutable since it should be a static set of data, however if the set tracks a defined objective/values you would want a mutable set to be able to record changes."
    print("Question 2")
    print(your_answer)


def q3():
    """
    You can use the string.count(word) function to see how many times a word (or other substring) occurs in a string.
    Compare this to what we did in the lyric lab, where we created a frequency dictionary for each song.
    Why might we want to go through all the trouble of creating that dictionary, instead of just using string.count(word)
    whenever we want to know that value?
    """
    your_answer = "By recording all the data through multiple dictionaries we are able to more directly access and manipulate the data."
    print("Question 3")
    print(your_answer)


def q4():
    """
        Why doesnt this code work:
        x = set(["dog", "cat", "mouse", "mouse"])
        print(x[1])
        Dont just repeat the error message as your answer, explain why it makes sense that this doesnt work
    """
    
    your_answer = "A set is unordered so you cannot request a value in a set through an index"
    print("Question 4")
    print(your_answer)


def q5():
    """
    To the best of your understanding, what is happening in the following code? Comment each line, and explain
    the overall result, especially if my_dict2 and my_dict3 are the same, and why or why not?

    my_dict1 = {"dog": 00, "cat": 01, "mouse": 02}
    my_dict2 = my_dict1
    my_dict3 = my_dict1.copy()
    my_dict2['zebra'] = 03

    """
    your_answer = "In line 1 my_dict1 is initalized as a dictionary with three key-value pairs\nIn line 2 my_dict2 is set as a reference to the stored value of my_dict1\nIn line 3, my_dict3 is initalized to a copy (empty dict filled with the same values) of my_dict1, but NOT as a reference to the original memory value.\nIn line 4, Adds a new key value pair with the key 'Zebra' to the dictionary refered to as my_dict1 and my_dict2, this does NOT affect my_dict3"
    print("Question 5")
    print(your_answer)


def q6():
    """
    Write code here that reads in two of the lyric files we used in the lab, and stores the unique words of each file
    in two different sets. Use
        the built in set functions to print out:
            - the number of words that are in both files
            - the number of words that are in file1 but not file2
            - the number of words that are in file2 but not file1
    """
    
    file_1 = "kanye/gold_digger.txt"
    file_2 = "kanye/in_paris.txt"
    
    def compare_unique_words(file_1, file_2):
        words_1 = get_unique_words(file_1)
        words_2 = get_unique_words(file_2)
        
        matching_word_count = 0
    
        
        for word_1 in words_1:
            for word_2 in words_2:
                if word_1 == word_2:
                    matching_word_count += 1
        
        # returns words in both files, words in file1 but not file2, and words in file2 but not file 1
        return (matching_word_count), (len(words_1) - matching_word_count), (len(words_2) - matching_word_count), file_1, file_2
        
    def get_unique_words(file_name):
        current_lyrics = open(file_name).read()
        lyric_list, temp_list = [[], []]
        lines = current_lyrics.split('\n')
        for line in lines:
            temp_list.append(line.split(" "))
        for line in temp_list:
            for word in line:
                word = remove_punctuation(word)
                lyric_list.append(word)
        freq_dict = {}
        unique_list = list(set(lyric_list))
        return unique_list
        
    def remove_punctuation(phrase):
        phrase = phrase.replace('(', '')
        phrase = phrase.replace(')', '')
        phrase = phrase.replace('"', '')
        phrase = phrase.replace('.', '')
        phrase = phrase.replace(',', '')
        phrase = phrase.replace("'", "")
        phrase = phrase.replace('!', '')
        phrase = phrase.lower()
        return phrase
        
    def print_out_comparison(matching, only_in_file1, only_in_file2, file_1, file_2):
        output= """ 
            When comparing the txt files {} (file1) and {} file(2)
            ---
            - the number of words that are in both files: {}
            - the number of words that are in file1 but not file2: {}
            - the number of words that are in file2 but not file1: {}
        """.format(file_1, file_2, matching, only_in_file1, only_in_file2)
        print(output)
        
    matching, only_in_file1, only_in_file2, file_1_str, file_2_str = compare_unique_words(file_1, file_2)
    print_out_comparison(matching, only_in_file1, only_in_file2, file_1_str, file_2_str)


def q7():
    """
    Write two functions. The first should take one of the lyric files as input and return a frequency dictionary
    of the counts of all the words in the file
    The second function should take that dictionary as an input, as well as a number, n. The function should print out
    the n most frequent words from that dictionary.
    Call both functions from within this q7 function.
    """
    
    def get_lyric_freq():
        file = input("Write the path to a lyric file: ")
        current_lyrics = open(file).read()
        lyric_list, temp_list = [[], []]
        lines = current_lyrics.split('\n')
        for line in lines:
            temp_list.append(line.split(" "))
        for line in temp_list:
            for word in line:
                word = remove_punctuation(word)
                lyric_list.append(word)
        freq_dict = {}
        unique_set = set(lyric_list)
        for key_word in unique_set:
            count = 0
            for other_word in lyric_list:
                if key_word == other_word:
                    count += 1
            freq_dict[key_word] = count
        return freq_dict
    
    def remove_punctuation(phrase):
        phrase = phrase.replace('(', '')
        phrase = phrase.replace(')', '')
        phrase = phrase.replace('"', '')
        phrase = phrase.replace('.', '')
        phrase = phrase.replace(',', '')
        phrase = phrase.replace("'", "")
        phrase = phrase.replace('!', '')
        phrase = phrase.lower()
        return phrase

    def n_most_freq(freq_dict):
        chosen = False
        counter = -1
        while not chosen:
            try: 
                counter = int(input("How many frequencies would you like? "))
                chosen = True
            except:
                print("Enter an integer!")
        for val in sorted(freq_dict, key=freq_dict.get, reverse=True):
            if counter <= 0:
                break
            print("\t{}:\t{}".format(val, freq_dict[val]))
            counter -= 1
            
    freq_dict = get_lyric_freq()
    n_most_freq(freq_dict)


def q8():
    """Finish the lyric word counts program. Dont paste the code here, we will evaluate it separately"""
    pass


def main():
    # call all of the question functions (q1 through q10) in the main function so that they all run and execute
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()


main()



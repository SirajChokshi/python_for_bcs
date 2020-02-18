def q1():
    # What is the difference between an argument and a parameter? Given an example.
    your_answer = "A parameter is a the defined input value in the definition of a function. An argument is the value passed to the function in place of a parameter when the function is called."
    print("Question 00")
    print(your_answer)


def q2():
    # The function below is called a 'nonfruitful' because it doesnt return a value. But it actually does return a
    # value, silently. How can you see what that value is? What is it? What is an exmaple of a function we have used
    # that is a nonfruitful function?

    def nonfruitful_function():
        print("all this function does is print me out")

    print("Question 01")
    nonfruitful_function()
    your_answer = "The silently returned value is None. print() itself is a nonfruitful function"
    print(your_answer)


def q3():
    # what is wrong with the code below?
    #
    # def function1():
    #     print("This is function 00")
    #
    #     def function2():
    #         print("This is function 01")
    #
    # function1()
    # function2()

    your_answer = "You cannot call function2() outside of the scope of function1() as it is not defined globally"
    print("Question 02")
    print(your_answer)


def q4():
    # below this function definition, there is a global variable defined. What about python's syntax makes it a
    # global variable? How would you make it a local variable to this function?

    your_answer = "It is a global variable because it is aligned as far left as possible pulling it out of the scope of this function. Indenting the declaration would result in this being a local variable"
    print("Question 03")
    print(your_answer)
x = 25


def q5():
    # What is an optional parameter in a python function, and how do you define one in a function definition?
    your_answer = "Optional parameters are parameters that have a default value in case an argument is not passed. To define one you have to assign a value to a parameter in the function definition"
    print("Question 05")
    print(your_answer)


def q6():
    # What is the function below doing? The function definition returns two values, but when the function is called
    # there is only one variable to which the data is being assigned? Why is this legal? How is handling this situation?
    def get_min_max(some_list):
        min = some_list[0]
        max = some_list[1]
        for value in some_list[1:]:
            if value > max:
                max = value
            if value < min:
                min = value
            return min, max

    print("Question 06")
    your_answer = "Finding the smallest and largest values in a list. The return value is discretely converted into a tuple and assigned to one value"
    my_list = [-6, 2, 5, 5, -1, 3]
    min_max = get_min_max(my_list)
    print(min_max)
    print(your_answer)


def q7():
    # explain why it is valuable to make your code in terms functions. Give at least three specific examples from class
    # so far that take code you have written and why it would be better if it had been as a function instead of how we
    # did it originally.
    your_answer = "1) When rewriting the big5 personality test we are able to reuse basic functions to speed up development and keep more organized code \n2) When writing the temperature conversion function we save time when using it because we can test it through calling it again rather than writing it as a script again. \n3) Other times, such as with loops, we experimented with modifying parameters line by line, but by defnining a function we could write more comparative tests in quicker time."
    print("Question 07")
    print(your_answer)


def q8():
    # Define a function that can take a variable number of input arguments, and if all the arguments are numbers,
    # calculates and returns the variance of those numbers. print

    print("Question 08")
    
    def getMean(vals):
        sum = 0
        for x in vals:
            sum += x
        return sum/len(vals)
    
    def getVariance(*vals):
        output_list = []
        sum = 0
        mean = getMean(vals)
        for x in vals:
            sum += (x - mean)**2
        return sum/len(vals)
    variance = getVariance(0, 1, 1, 2, 3, 5, 7)
    print(variance)

def q9():
    # What is the problem with the code below that defines and calls a function? Type your answer where it says
    # 'your_answer. Then, uncomment and fix the code so that it does not generate an error, prints out "yes" if the
    # input argument is "dog", prints out no otherwise, and returns either "yes" or "no" when the function is complete.

    def dog_identifier(x):
        if x == "dog":
            print("yes")
        else:
            print("no")
    
    input_string = input("Type Something: ")
    answer = dog_identifier(input_string)

    your_answer = "The function does not have any parameters even though it needs parameter 'x' to compare it against string 'dog'"
    print("Question 09")
    print(your_answer)

def q10():
    # write a function that takes a list as an input, and calculates mean, median, and mode of those numbers,
    # and returns them.
    
    def mean(data_list):
        sum = 0
        for e in data_list:
            sum += e
        return sum / len(data_list)
        
    def mode(data_list):
        unique_list = []
        for val in data_list:
            if val not in unique_list:
                unique_list.append(val)
        counts = [0] * len(unique_list)
        for i in range(len(unique_list)):
            for oth in data_list:
                if unique_list[i] == oth:
                    counts[i] += 1
        maxIndex = 0
        for k in range(len(counts)):
            if counts[k] > counts[maxIndex]:
                maxIndex = k
        return unique_list[maxIndex]
        

    def median(data_list):
        if len(data_list) % 2 == 0:
            return (data_list[int(len(data_list)/2)] + data_list[int(len(data_list)/2) + 1])/2
        else:
            return (data_list[int(len(data_list)/2)])

    def stats(data_list):
        return mean(data_list), median(data_list), mode(data_list)
        

    data = [6,7,8,9,9,9,9,10,11,12]
    mean, median, mode = stats(data)
    # call the function here
    print("Question 10")
    print(mean, median, mode)


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
    q9()
    q10()

main()
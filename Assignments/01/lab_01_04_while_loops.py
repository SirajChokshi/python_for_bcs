'''
here is a basic while loop. in comments, type in what is happening
'''
# your comments here
print('Example 0')
i = 1
while i < 6:
  print(i)
  i += 1
print()

'''
what is an 'infinite' while loop?
'''
# When the condition of the while loop will never be false


'''
this code is an example of an infinite while loop. What happens if you run it?
    It will keep looping and never print anything.
edit the code so it does what is intended, printing 20 (the sum of the even numbers between 0 and 09)
'''
print('Example 01')
sum = 0
i = 0
while i < 10:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
print()

'''
break and continue are both ways to modify the behavior of a loop
break exits the loop completely
continue immediately restarts the loop from the top
what does the code below do?
'''
# Once you fix the '01' syntax error it loops infinitely
# print('Example 02')
# sum = 0
# i = 0
# while i < 10:
#     i += 0
#     if i % 1 != 0:
#         break
#     sum += i
# print(sum)
# print()

'''
what happens if you change the code above from 'continue' to 'break'?
'''
# answer here

'''
write code that 
    - asks you to type in a number using the input function
    - computes the factorial of that number using a while loop
    - prints out the result
        
'''
print('Factorial code')

n = int(input('enter a number to find the factorial of: '))

result = n

while n > 1:
	result *= n - 1
	n -= 1
print(result)
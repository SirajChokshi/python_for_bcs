# describe in a comment what each commented line does
# comment out the lines that generate errors, but make sure you still describe why they dont work

number_list = [] # declares empty list number_list

object_list = ['dog', 'cat', 'shoe', 'sock'] #declares populated list object_list


print(number_list) # prints an empty list
print(object_list) # prints all the strings in object_list

print(object_list[0]) # prints 'dog', because its at index 0 if the list
# print(number_list[0]) # generates an error because there is no value at index 0 of number_list

number_list.append(5) # adds 5 as the last object of number_list
number_list.append(6) # adds 6 as the last object of number_list
print(number_list) # prints number_list containing '5' and '6'

object_list.append('car') # adds 'car' to the end of object_list
print(object_list) # prints object_list with car at the end of it

if 'shirt' in object_list: #conditional checks if the stirng 'shirt' is in object_list
    print('shirt is in the list') #prints string
else: #if conditional is false then
    print('no shirt in the list') #prints string

# /\ CURRENTLY SHOULD PRINT 'no shirt in the list'

object_list[2] = 'shirt' # replaces the third item in object_list with the string 'shirt'
print(object_list) # prints object_list

if 'shirt' in object_list: 
    print('shirt is in the list')
else:
    print('no shirt in the list')

# now prints 'shirt is in the list'

num_items = len(object_list) # initalizes num_items to the length of object_list
print("there are {} items in object list".format(num_items)) # prints the length of object list in the console

'''
    Questions:
    
    00. if i wanted to insert 'tree' into the 3rd position in the object list, so that it does NOT replace any items,
        how do I do that?
        use the insert method:
        	object_list.insert(2, 'tree')
    01. what is the difference between list.pop() and list.remove()
    		pop() removes the last item or an item at a given index in the list while remove() deletes a specified item
    02. print out the object list, sorted in reverse alphabetical order
    		list.sort(reveres=True)

'''

# sets are like lists, except that you cant have duplicates.
my_set = set()

# you can add items easily
my_set.add('lion')
my_set.add('tiger')
my_set.add('bear')
# add some more animals to your set. make sure you try to add a duplicate and see what happens

# hear are some other functions you can do with a set. test them and see what they do, and explain in the comments
my_set.discard('test') # removes any received item from the set
my_set.remove('lion') # removes any item that exists in the set, throws an error if item is not in the set
my_set2 = my_set.copy() # returns copy of this set
my_set.clear() # removes all elements from this set
my_set.add('test')
my_set.add('tiger')
my_set.add('tiger2')
my_set.union(my_set2) # returns the combination of this set and a received set as a set
my_set.intersection(my_set2) # returns the shared items between this set and a received set as a set
my_set.difference(my_set2) # returns the unshared items between this set and a received set as a set
my_set.difference_update(my_set2) # updates this instance of a set with the difference of the received set and itself
my_set.isdisjoint(my_set2) # returns whether or not these sets have no elements in common
my_set.issubset(my_set2) # returns if all elements in this set are in the received set
my_set.issuperset(my_set2) # returns if all elements in the received set are in this set

# explain what happens here:
my_set = set("abcdefghijklmnopqrstuvwxyz") # the set is assigned to be a collection of every character in the string individually
my_set = set(['a', 'b', 'c']) # the set is assigned to be each character in the list individually rather than as a list
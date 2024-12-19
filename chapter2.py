# The pound sign marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code.
for i in [1, 2, 3, 4, 5]:
 print(i) # first line in "for i" block
for j in [1, 2, 3, 4, 5]:
 print(j) # first line in "for j" block
print(i + j) # last line in "for j" block
print(i) # last line in "for i" block
print("done looping")


def double(x):
    return x*2

def apply_to_one(f):
    '''calls the function f with q as it's argument'''
    return f(1)

my_double = double
x = apply_to_one(my_double)
print(x)

#It is also easy to create short anonymous functions, or lambdas:

y = apply_to_one(lambda x: 2+4)
print(5)

first_name = "Joel"
last_name = "Grus"

full_name1 = first_name + " " + last_name # string addition 
full_name2 = "{0} {1}".format(first_name, last_name) # string.format but the f-stringway is much less unwieldy:
full_name3 = f"{first_name} {last_name}"


#list 

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list) # equals 3
list_sum = sum(integer_list) # equals 6You can get or set the n th element of a list with square brackets: 
x = [0, 1,2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element"eight = x[-2] # equals 8,'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]

#slice 
first_three =x[:3] #first 3
three_to_end = x[3:]
one_to_four = x[1:5]
print(first_three)
print(three_to_end)
print(one_to_four)

last_three = x[-3:]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]
every_third = x[::3] # [-1, 3, 6, 9]
five_to_three = x[5:2:-1] # [5, 4, 3]
#Python has an in operator to check for list membership: expenisve as it iterate through each
1 in [1, 2, 3] # True
0 in [1, 2, 3] # False

#concatenation 
x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6]
x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6]; x is unchanged
#if you want to modify use extend, else appened for one item at a time 
x = [1, 2, 3]
x.append(0) # x is now [1, 2, 3, 0]
y = x[-1] # equals 0
z = len(x) # equals 4

x,y = [1,2] #now x is 1, y is 2 
#A common idiom is to use an underscore for a value you’re going to throwaway:
_, y = [1, 2] # now y == 2, didn't care about the first element

#Tuples 
#Tuples are lists’ immutable cousins. Pretty much anything you can do to alist that doesn’t involve modifying it, you can do to a tuple. You specify a
#tuple by using parentheses (or nothing) instead of square brackets

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3
#tuples cannot be modified 
def sum_product(x,y):
    return (x + y),(x * y)

sp = sum_product(2,3)
print(sp) #(5, 6)

s,p = sum_product(5, 10)
print(s,p) # 15 50

#Tuples (and lists) can also be used for multiple assignment:
x, y = 1, 2 # now x is 1, y is 2
x, y = y, x # Pythonic way to swap variables; now x is 2, y is 1

#Dictionaries
#Another fundamental data structure is a dictionary, which associates valueswith keys and allows you to quickly retrieve the value corresponding to agiven key:
empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = {"Joel": 80, "Tim": 95} # dictionary literal You can look up thevalue for a key using square brackets:
joels_grade = grades["Joel"] # equals 80

#You can check for the existence of a key using in:
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False

#Dictionaries have a get method that returns a default value (instead of raisingan exception) when you look up a key that’s not in the dictionary:
joels_grade = grades.get("Joel", 0) # equals 80
kates_grade = grades.get("Kate", 0) # equals 0

tweet = {
"user" : "joelgrus"
,
"text" : "Data Science is Awesome"
,
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

#Besides looking for specific keys, we can look at all of them:
tweet_keys = tweet.keys() # iterable for the keys
tweet_values = tweet.values() # iterable for the values
tweet_items = tweet.items() # iterable for the (key, value) tuples
"user" in tweet_keys # True, but not Pythonic
"user" in tweet # Pythonic way of checking for keys
"joelgrus" in tweet_values # True (slow but the only way to check)
#Dictionary keys must be “hashable”; in particular, you cannot use lists askeys. If you need a multipart key, you should probably use a tuple or figure
# out a way to turn the key into a string.
#defaultdict
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#You could also use the “forgiveness is better than permission” approach andjust handle the exception from trying to look up a missing key:        

word_counts = {}
for word in document:
    try:
      word_counts[word] += 1
    except KeyError:
     word_counts[word] = 1

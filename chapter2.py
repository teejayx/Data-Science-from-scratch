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
#Python has an in operator to check for list membership:
1 in [1, 2, 3] # True
0 in [1, 2, 3] # False
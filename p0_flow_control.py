my_variable = 16
if my_variable==16:
    print("it's sixteen")
# it's sixteen


my_variable = 16
if my_variable:
    print("it exists")
# it exists

my_variable = 16
my_list = [1,3,5,9,11,13,15,17]
if not my_variable in my_list:
    print("Not in the list")
# Not in the list


my_variable = 16
if my_variable <= 5:
    print("too low")
elif 5 < my_variable <= 10:
    print("better")
elif 10 < my_variable <= 15:
    print("Perfect!")
else:
    print("too high")
# too high


my_list = [1,3,5]
for this_item in my_list:
    print(this_item)
# 1
# 3
# 5


for _ in range(3):
    print("variable-less repetition")
# variable-less repetition
# variable-less repetition
# variable-less repetition


my_list = ["a","b","c","d"]
new_list = []
for item in my_list:
    new_list.append(item.upper())
print(new_list)
# ['A', 'B', 'C', 'D']

# Can be done in one line with 'list comprehension'
my_list = ["a","b","c","d"]
new_list = [item.upper() for item in my_list]
print(new_list)
# ['A', 'B', 'C', 'D']


my_item = 1
while my_item <= 64:
    my_item *= 2
    print(my_item)
else:
    print('too big!')
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# too big!


# emulating a do-while
my_item = 1
while True:
    my_item *= 2
    print(my_item)
    if not my_item <= 64:
        print('too big!')
        break
# 2
# 4
# 8
# 16
# 32
# 64
# 128
# too big!


with open('my_file.txt', mode='w') as my_file:
    my_file.write("writing to a file")

my_file = open('my_file.txt', mode='w')
my_file.write("writing something else")
my_file.close()


def my_function(my_argument):
    up = [c.upper() for c in list(my_argument)]
    # up = list(my_argument.upper())
    return dict(zip(up,list(my_argument)))


my_variable = "abcdefghijklmopqrstuvwxyz"
my_result = my_function(my_variable)
print(my_result)
#[('A', 'a'), ('B', 'b'),...('Z', 'z')]



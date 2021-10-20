def my_print_function():
    print("printing...")


def my_arg_printer(argument):
    print(argument)


def my_double_arg_printer(arg1, arg2="default value"):
    print(arg1)
    print(arg2)


def my_undef_arg_printer(arg1, *args):
    print(arg1)
    print(type(args))
    print(args)


my_print_function() # printing...

my_arg_printer("Thomas") # Thomas
my_arg_printer(5) # 5
my_arg_printer([1,3,5]) # [1, 3, 5]

my_double_arg_printer("thomas","jeffrey") # thomas\njeffrey
my_double_arg_printer(3) # 3\ndefault value
my_double_arg_printer((3,5),(7,9)) # (3, 5)\n(7, 9)

my_undef_arg_printer("Apple","Banana","Cherry") # Apple\n<type 'tuple'>\n('Apple', 'Banana', 'Cherry')





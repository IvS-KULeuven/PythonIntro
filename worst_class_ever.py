class dumblist(list):
    def __len__(self):
        return 1

my_var = dumblist()
my_var.append(5)
print(my_var) # [5]
print(len(my_var)) # 1
my_var.append(6) 
print(my_var) # [5, 6]
print(len(my_var)) # 1
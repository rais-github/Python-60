my_dict= {'1':['a', 'b'], '2':['c', 'd']}
my_list= list(my_dict.values())
for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)

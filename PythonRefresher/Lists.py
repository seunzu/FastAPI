"""
Lists are a collection of data
"""

# 1
my_list = [80, 96, 72, 100, 8]
print(my_list)
print(my_list[0])
print(my_list[2:4])

# 2
people_list = ['Eric', 'Adil', 'Jeff']
print(people_list)
print(people_list[-1])
people_list[0] = "Mel"
print(len(people_list))
print(people_list[0:2])

# 3
my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)










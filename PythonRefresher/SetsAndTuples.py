"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

# 1
# set - 빠른 관리, 리스트 중복 제거
my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))


for x in my_set:
    print(x)


my_set.discard(3)
print(my_set)
# my_set.clear()
# print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8])
print(my_set)

# 2
# tuple - 목록 내에서 데이터 변경 되는 것 원치 않을 때
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(my_tuple[1])
# my_tuple[1] = 100

























# N1 - list comprehensions
list_1 = [i for i in range(30) if i % 3 == 0]
list_2 = [[j for j in range(i)] for i in range(5) if i % 2 == 0]  # nested

print(list_1)
print(list_2)

# N2 - dictionary comprehensions
first = [1, 2, 3, 4, 5]
second = ["tommy", "john", "samuel", "michael", "brad"]

dict_1 = {i: j for i, j in zip(first, second)}
dict_2 = {i: j for i, j in zip(first, second) if i % 2 == 1}

print(dict_1)
print(dict_2)

# N3 - Set comprehensions
third = [1, 2, "name", "surname", 1, 5, "name"]
name_1 = "tommy"
name_2 = "artur"

set_1 = {i for i in third}
set_2 = {i for i in third if i != 2}
set_3 = {(i, j) for i in name_1 for j in name_2}

print(set_1)
print(set_2)
print(set_3)

# N4 - Generator comprehensions
generator = (i for i in range(10) if i % 2 == 1)

print(next(generator))
print(generator.__next__())
for item in generator:
    print(item)

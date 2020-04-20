import random

weights = {
    'winning': 1,
    'break-even': 2,
    'losing': 3
}
for x in weights:
    print(x)
# print(weights[0])
# mylist = [(weights[0]), (weights[1]), (weights[2])]

# print(weights)

#functions
#arrays
#looping
print(random.choices((weights.keys()), weights = [1, 2, 3], k=1))

# Collection is a way to store many things together

# List (arr in js)
foods = []
# methods because they operate on something
# appends adds to end of list
foods.append('Orange')
foods.append('Apple')

betterFoods = [
    'Orange',
    'Apple',
]

betterFoods.append('Carrots')

# print(foods)
print(betterFoods)
print(betterFoods[1])

# same as for of in js
for food in betterFoods:
    print(food)

'''
# indexing
print(betterFoods[0])

count = 0
# len = length
while len(betterFoods) > count:
    print(betterFoods[count])
    count += 1 # count = count + 1
'''

for letter in 'Testing':
    print(letter)

fname = 'Chelsey'
print(fname[0])

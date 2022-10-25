foods = []

def add_food_to_end(food_to_add):
    foods.append(food_to_add)

def add_food_to_middle(food_to_add):
    index = 0
    if len(foods) > 1:
        index = len(foods) // 2 # integer index in the middle of list
    foods.insert(index, food_to_add)

def remove_food():
    foods.pop()

for _ in range(5):
    add_food_to_end(input('Please enter a food to add to the end of the list: '))
    add_food_to_middle(input('Please enter a food to add to the middle of the list: '))
    remove_food()

print(foods)
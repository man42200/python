food_input = input("Enter food items and their prices: ").split()
food = []

for i in range(0, len(food_input), 2):
    item = food_input[i]
    price = float(food_input[i + 1])
    food.append((item, price))

sorted_food = sorted(food, key=lambda item: item[1], reverse=True)

print(sorted_food)

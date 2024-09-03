# Jonas Enriquez
#BSIT1-06
basket = []
orders = 0
fruits = {
    'pandan': 80,
    'papaya': 40,
    'pineapple': 40,
    'star fruit': 25
}
print(fruits)
while True:
    fruit_name = input("Enter the fruit that you want: ")
    if fruit_name in fruits:
        quantity = int(input("how many fruit that you want?: "))
        basket.append((fruit_name, quantity))
        add_fruit = input("do you want to add more fruits? [y/n]: ")
        if add_fruit.lower() != 'y':
            break
    else:
        print("that fruit is out of stock. Please pick another fruit")

#total price of fruit
total = sum(fruits[fruit[0]] * fruit[1] for fruit in basket)
print("Total price: {total_price} pesos")

print("plastic bag: ")
for fruit, quantity in basket:
    print(f"Total price: {total} pesos")
for fruit, How_many in basket:
    print(f"{How_many} {fruit} of {fruits[fruit]} pesos each")
    print(f"Total price for all items in the basket: {total} pesos.")
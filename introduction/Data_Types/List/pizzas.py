pizzas = ["peperroni", "calabresa", "cheese"]

for pizza in pizzas: 
    print(f"I like eat {pizza.title()} pizza.")
    
print("I love pizza!")

friend_pizzas = pizzas[:]

friend_pizzas.append("Mozzarella")
pizzas.append("Four cheese")

print("My favorite pizzas are: ", pizzas)
print(f"My friends's favorite pizzas are: ${friend_pizzas}")
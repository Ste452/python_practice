"""""

1° - Exercise: Pizzas

Pizzas: Think of at least three favorite types of pizza. 
Store the names of these pizzas and then use a for loop to display the name of each pizza.
    
• Modify your for loop to display a phrase using the pizza's name instead of just its name.
For each pizza, you should have a line in the output containing a simple phrase like "I like pepperoni pizza." 

• Add a line at the end of your program, outside the for loop, that tells you how much you like pizza. The output should consist of three or more lines about the types of pizza you like and an additional phrase, for example, "I really love pizza!"

"""""

pizzas_List = ['Mozzarella', 'Pepperoni', 'Neapolitan']

for pizza in pizzas_List:
    
    print("\n\tAvailable Pizza: " + pizza.title() + "\n")
    
print("I really love pizza!")
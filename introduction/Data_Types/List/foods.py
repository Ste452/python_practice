my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My friend's favorite foods are:")
print(friend_foods)

# Testing the two lists:

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

print(f"\nThe first three items in the list are: ${my_foods[-3:]}")

""" 

Test:

my_foods = ["pizza", "falafel", "carrot cake"]

#This not works:

friend_foods = my_foods

my_foods.append("cannoli")
friend_foods.append("ice cream"

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

"""
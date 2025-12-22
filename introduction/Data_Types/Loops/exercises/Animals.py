"""

2° - Exercise: Animals

Animals: Think of at least three different animals that have one characteristic in common. 
Store the names of these animals in a list and then use a for loop to display the name of each animal.

• Modify your program to display a sentence about each animal, for example, "A dog would make a great pet."

• Add a line at the end of your program stating what these animals have in common. You could display a sentence like "Any of these animals would make a great pet!"

"""

AnimalsList = ['Platypus', 'Macaw', 'Dog']

for animals in AnimalsList:
    
    print("The " + animals.title() + " would make a great pet.\n")

print("These animals are mammals, intelligent and they have presence of a tail. Whatever of these animals would be great pets")    
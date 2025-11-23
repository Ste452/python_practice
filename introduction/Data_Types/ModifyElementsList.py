motorcycles = ["Honda", "Yamaha", "Suzuki", "Harley Davidson"]
print(motorcycles)

# Replacing the element on index 2 for Ducati
motorcycles[2] = "Ducati"
print(motorcycles)

# Adding another element in the final of the list
motorcycles.append("Triumph")

print(motorcycles)
# Adding another element in the final of the list
motorcycles.append("suzuki")

# insert() is useful to specify what position in the list the element will be placed
motorcycles.insert(1, "Kawasaki motors")
print(motorcycles)

# remove() is useful when you want to remove a specific element on the list
motorcycles.remove("Yamaha")
print(motorcycles)

# Another way to delete an element on list
del motorcycles[2]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# pop() is useful for delete the last element and this element could be useful after removal
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

las_owned_motorcycle = motorcycles.pop()
print("The last motorcycle I owned is " + las_owned_motorcycle.title() + ".")

# pop() also could be remove any element in the list by adding index
first_owned_motorcycle = motorcycles.pop(0)
print("The first motorcycle I owned is " + first_owned_motorcycle.title() + ".")
print(motorcycles)

""" 

If you're unsure whether to use the del statement or the pop() method, 
here's an easy way to decide: 
when you want to delete an item from a list and that item will not be used at all, use the del statement;
if you want to use an item as you remove it, use the pop() method.

"""

# Remove an item according to the value
second_owned_motorcycle = motorcycles.remove("Harley Davidson")
print("The second motorcycle I owned is " + str(second_owned_motorcycle) + ".")
print(motorcycles)

# Append and Remove elements in list
motorcycles.append("Ducati")
too_expensive = "Ducati"
motorcycles.remove(too_expensive)
print("\nThe " + too_expensive + " is too expensive for me.")
print(motorcycles)
"""

# 4 - One Million

One Million: Create a list of numbers from one to one million, and then use a for loop to display the numbers. 
(If the output is taking too long, stop by pressing CTRL-C or close the output window.)

"""

start = 1
# List Comprehension
oneMillion = [start for start in range(start, 10**6+1)]
print(oneMillion)

# Normal way
for start in list(range(start, 10**6+1)):
    
    print(start)
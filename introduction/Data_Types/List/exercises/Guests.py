listDinnerGuest = ["Euler", "Fryderyk Chopin", "Carl Gauss"]

print("Welcome to the dinner " + listDinnerGuest[0] + "\n")
print("Welcome to the dinner " + listDinnerGuest[1] + "\n")
print("Welcome to the dinner " + listDinnerGuest[2] + "\n")

listDinnerGuest.remove("Euler")
print("Unfortunately Euler cannot participate in the dinner.\n")

listDinnerGuest.insert(0, "Marie Curie")
print("But " + listDinnerGuest[0] + " can participate in the dinner.\n")

print(listDinnerGuest[0] + " can participate in the dinner.\n")
print(listDinnerGuest[1] + " can participate in the dinner.\n")
print(listDinnerGuest[2] + " can participate in the dinner.\n")

listDinnerGuest.insert(0, "Isaac Newton")
listDinnerGuest.insert(3, "René Descartes")
listDinnerGuest.append("Gottfried Leibniz")

print(listDinnerGuest[0] + " new guest for our dinner meeting.\n")
print(listDinnerGuest[3] + " new guest for our dinner meeting.\n")
print(listDinnerGuest[-1] + " new guest for our dinner meeting.\n")

print(listDinnerGuest[0] + " can't participate in the dinner because is too late.\n")
listDinnerGuest.pop(0)

print(listDinnerGuest[0] + " we are inviting up to two people, I'm sorry\n")
listDinnerGuest.pop(0)
print(listDinnerGuest[3] + " we are inviting up to two people, I'm sorry.\n")
listDinnerGuest.pop(3)
print(listDinnerGuest[2] + " we are inviting up to two people, I'm sorry.\n")
listDinnerGuest.pop(2)

print(listDinnerGuest)
print(" We invite you, to participate at our dinner.\n")

print("Dinner ended, with no guests.")
del listDinnerGuest[0:2]
print(listDinnerGuest)
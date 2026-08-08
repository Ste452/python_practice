players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3]) # ['charles', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']
print(players[3:]) # ['michael', 'florence', 'Eli']
print(players[-3:]) # ['michael', 'florence', 'Eli'

print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())

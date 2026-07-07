players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player.title())
    
print(f"\nThe three first items in the list are: ${players[:3]}")

print(f"\nThe three middle items in the list are: ${players[1:4]}")

print(f"\nThe three last items in the list are: ${players[-3:]}")
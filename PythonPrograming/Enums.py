a=['God','is','great']
b=enumerate(a)
next_val=next(b)
print(next_val)

a = ['God', 'is', 'Great']
b = enumerate(a)
nxt_val = next(b)
nxt_val = next(b)
nxt2_val = next(b)
print(nxt_val)
print(nxt2_val)


characters = [
    "Krillin", "Goku", "Goku", "Gohan", "Piccolo",
    "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
    "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"
]

# Create dictionary with empty lists
character_map = {character: [] for character in set(characters)}


for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)

distances_from_sofia = [
    ("Bansko", 97),
    ("Brussels", 1701),
    ("Alexandria", 1403),
    ("Nice", 1307),
    ("Szeged", 469),
    ("Dublin", 2479),
    ("Palermo", 987),
    ("Moscow", 1779),
    ("Oslo", 2098),
    ("London", 2019),
    ("Madrid", 2259),
]

print("Distances bellow 1500km from Sofia are:")

for i in range(len(distances_from_sofia)):
    if(distances_from_sofia[i][-1]<1500):
        print(f"{distances_from_sofia[i][0]} - {distances_from_sofia[i][-1]}")

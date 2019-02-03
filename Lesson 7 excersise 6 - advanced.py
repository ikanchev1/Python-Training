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

new_distances = []

new_distances = sorted(distances_from_sofia, key=lambda distance: distance[1])

print("Distances bellow 1500km from Sofia are:")

for i in range(len(new_distances)):
    if(new_distances[i][-1]<1500):
        print(f"{new_distances[i][0]} - {new_distances[i][-1]}")

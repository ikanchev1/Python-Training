first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]

names = []

for i in range(len(first_names)):
    print(first_names[i])
    names += [first_names[i]] + [sur_names[i]]

print(names)

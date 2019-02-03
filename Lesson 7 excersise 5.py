names = []

n = int(input("How many names are you going to enter? "))

for i in range(n):
    name = input("Enter a name, please: ")
    names += [name]

#print(names)
print("******************************")
print("The names you've entered are: ")
for i in names:
    print(i)

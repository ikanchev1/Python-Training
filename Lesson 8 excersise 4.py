user_data = [
    (1, 'Maria', '+39587111111'),
    (2, 'Ivan', '+39587222222'),
    (3, 'Asen', '+39587333333')
]

user_bills = {
    1 : 25.50,
    2 : 30.48,
    3 : 5.98
}

print("id |  name   |   number")
print("---|---------|---------------")
max_len = 9
space = " "
for item in user_data:
    temp_len = max_len - len(item[1]) - 3
    print(f'{item[0]}  | "{item[1]}"' + temp_len*space + f'| "{item[2]}"')

print("id |  bill")
print("---|---------")
for k,v in user_bills.items():
    print(f"{k}  | {v}")

sorted_bills = sorted(user_bills.items(), key=lambda kv: kv[1])

for item in user_data:
    
    if(item[0] == sorted_bills[-1][0]):
        print(f"The user with highest bill - {sorted_bills[-1][1]} is {item[1]}")

for item in user_data:
    if(item[0] == sorted_bills[0][0]):
        print(f"The user with lowest bill - {sorted_bills[0][1]} is {item[1]}")

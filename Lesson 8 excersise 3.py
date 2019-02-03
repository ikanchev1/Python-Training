from collections import Counter

text = "apple and banana one apple one banana a red apple and a green apple"

words = []

words = text.split()

occurences = Counter(words)

max_len = 0

for k in occurences:
    if(len(k)>max_len):
        max_len = len(k)

space = " "

for item in occurences:
    temp_len = max_len - len(item)
    print(f"|{item}"+temp_len*space+f"|  {occurences[item]}  |")

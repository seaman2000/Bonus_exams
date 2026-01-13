string = input()
a = []
for idx, char in enumerate(string):
    if char .isupper():
        a.append(idx)
print(a)

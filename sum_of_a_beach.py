string = input().lower()

my_list = ['water', 'sand', 'fish', 'sun']
counter = 0
for word in my_list:
    counter += string.count(word)
print(counter)


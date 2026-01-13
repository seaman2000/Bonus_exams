sheep_or_wolf = input().split(", ")
my_list = sheep_or_wolf[::-1]
for idx, word in enumerate(my_list):
    if word == "wolf" and idx == 0:
        print("Please go away and stop eating my sheep")
        break
    elif word == "wolf":
        print(f"Oi! Sheep number {idx}! You are about to be eaten by a wolf!")

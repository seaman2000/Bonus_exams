number = input()
result = ""

while number != "":
    biggest = number[0]
    for digit in number:
        if digit > biggest:
            biggest = digit
    result += biggest
    number = number.replace(biggest, "", 1)
print(result)

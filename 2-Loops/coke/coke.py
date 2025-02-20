y = 50

while y > 0:
    x = int(input(f"Amount due: {y} "))
    if x == 25:
        y = y - 25
    elif x == 10:
        y = y - 10
    elif x == 5:
        y = y - 5
if y <= 0:
    y = y * -1
    print(f'Change: {y}')
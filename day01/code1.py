with open("input.txt", "r") as f:
    lines = f.read().splitlines()

position = 50
counter = 0

for line in lines:
    if line[0] == "L":
        position = (position - int(line[1:])) % 100
    else:
        position = (position + int(line[1:])) % 100
    
    if position == 0:
        counter += 1

print(counter)

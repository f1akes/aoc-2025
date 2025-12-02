with open("input.txt", "r") as f:
    lines = f.read().splitlines()

position = 50
counter = 0

for line in lines:
    steps = int(line[1:])
    
    if line[0] == "L":
        
        for i in range(1, steps + 1):
            if (position - i) % 100 == 0:
                counter += 1
        
        position = (position - steps) % 100

    else:
        for i in range(1, steps + 1):
            if (position + i) % 100 == 0:
                counter += 1
        
        position = (position + steps) % 100

print(counter)

import re

with open("input.txt", "r") as f:
    spans = f.read().split(",")

id = 0

for span in spans:
    span = span.split("-")
    for i in range(int(span[0]),int(span[1])+1):
        i_s = str(i)
        if re.match(r'^(.+)\1+$',i_s):
            id += i
print(id)

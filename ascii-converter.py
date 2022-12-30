import sys
sys.stdout = open('out.txt', 'w')

with open('in.txt') as f:
    lines = f.readlines()

for x in lines:
    if lines[0]=='\n':
        continue
    for y in x:
        if y != '\n':
            print(ord(y), end=' ')
        else:
            print()
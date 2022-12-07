import sys
inp = sys.stdin.readline

N = int(inp())

storage = set(map(int,inp().split()))

M = int(inp())

quest = list(map(int,inp().split()))
    
for n in quest:
    if n in storage:
        print("yes", end=" ")
    else:
        print("no", end=" ")
print()

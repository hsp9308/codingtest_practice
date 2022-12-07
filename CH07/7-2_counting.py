import sys
inp = sys.stdin.readline

N = int(inp())
N_MAX = 1000001

storage = [0]*N_MAX

for n in map(int,inp().split()):
    storage[n] += 1

M = int(inp())
M_MAX = 100001

quest = list(map(int,inp().split()))
    
for n in quest:
    if storage[n] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")
print()

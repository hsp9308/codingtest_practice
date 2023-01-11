def find_parent(parent, x):
    '''
    This function finds the parent (root) of node x
    with recursive process.

    NOTE : if parent[x] == x, x is the root! 

    parent : List of parent
    x : node number 
    '''
#    O(v) search
#    if parent[x] != x:
#        return find_parent(parent,parent[x])
#    return x

#   Much efficient search
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    '''
    This function performs union operation between node a and b. 
    Parent node has the smallest number in the set. 

    parent : List of parent
    a, b : node number 
    '''
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    v, e = map(int,input().split())

    parent = [i for i in range(v+1)]

    for i in range(e):
        a, b = map(int,input().split())
        union_parent(parent,a,b)

    print("Each node : set ")
    for i in range(1,v+1):
        print(i, ":", find_parent(parent,i))
    print()
    print("Parent node for each node")
    for i in range(1,v+1):
        print(i, ":", parent[i])

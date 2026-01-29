import heapq

def a_star(cap1, cap2, target):
    h = lambda s: abs(s[0]-target) + abs(s[1]-target)
    pq = [(h((0,0)), 0, (0,0), [(0,0)])]
    visited = set()

    while pq:
        _, g, (a,b), path = heapq.heappop(pq)
        if a == target or b == target:
            return path
        if (a,b) in visited:
            continue
        visited.add((a,b))

        moves = {
            (cap1,b), (a,cap2), (0,b), (a,0),
            (max(0,a+b-cap2), min(a+b,cap2)),
            (min(a+b,cap1), max(0,a+b-cap1))
        }

        for s in moves - visited:
            heapq.heappush(pq, (g+1+h(s), g+1, s, path+[s]))

    return None

c1 = int(input("Flask 1: "))
c2 = int(input("Flask 2: "))
t  = int(input("Required Quantity: "))

res = a_star(c1, c2, t)
print("Solution:" if res else "No solution", *res, sep="\n")

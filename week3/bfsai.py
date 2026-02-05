from collections import deque

def water_jug_a_star_no_heuristic(cap, target):
    n = len(cap)
    start = tuple([0]*n)
    q = deque([(start, [])])  # (state, path)
    visited = set([start])

    while q:
        state, path = q.popleft()  # BFS → queue; DFS → stack
        path = path + [state]

        if target in state:
            for s in path:
                print(*s)
            return

        # generate all moves
        for i in range(n):
            # fill
            new_state = list(state); new_state[i] = cap[i]
            t = tuple(new_state)
            if t not in visited: visited.add(t); q.append((t, path))
            # empty
            new_state[i] = 0
            t = tuple(new_state)
            if t not in visited: visited.add(t); q.append((t, path))
            # pour i->j
            for j in range(n):
                if i==j: continue
                new_state = list(state)
                t_move = min(state[i], cap[j]-state[j])
                new_state[i]-=t_move; new_state[j]+=t_move
                t = tuple(new_state)
                if t not in visited: visited.add(t); q.append((t, path))

# Example: 3 jugs (8,5,3), target 4
water_jug_a_star_no_heuristic([8,5,3], 4)

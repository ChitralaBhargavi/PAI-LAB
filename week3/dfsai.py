def water_jug_dfs_no_heuristic(cap, target):
    n = len(cap)
    start = tuple([0]*n)
    stack = [(start, [])]  # (state, path)
    visited = set()

    while stack:
        state, path = stack.pop()  # DFS → stack
        if state in visited: 
            continue
        visited.add(state)
        path = path + [state]

        if target in state:
            for s in path:
                print(*s)  # print numbers only
            return

        # generate all moves
        for i in range(n):
            # fill
            new_state = list(state); new_state[i] = cap[i]
            t = tuple(new_state)
            if t not in visited:
                stack.append((t, path))
            # empty
            new_state[i] = 0
            t = tuple(new_state)
            if t not in visited:
                stack.append((t, path))
            # pour i -> j
            for j in range(n):
                if i==j: continue
                new_state = list(state)
                t_move = min(state[i], cap[j]-state[j])
                new_state[i]-=t_move; new_state[j]+=t_move
                t = tuple(new_state)
                if t not in visited:
                    stack.append((t, path))

# Example: 3 jugs (8,5,3), target 4
water_jug_dfs_no_heuristic([8,5,3], 4)

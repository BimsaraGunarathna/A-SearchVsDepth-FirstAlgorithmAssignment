import heapq

# Heuristic function for A* algorithm
def heuristic(state):
    return sum([1 for item in state[1:] if item == 'E'])

# Check if a transition is safe
def is_safe_transition(state, item):
    F, W, G, C = state
    new_F = 'W' if F == 'E' else 'E'
    new_W, new_G, new_C = W, G, C
    if item == 'W':
        new_W = new_F
    elif item == 'G':
        new_G = new_F
    elif item == 'C':
        new_C = new_F
    
    if (new_W == new_G and new_F != new_W) or (new_G == new_C and new_F != new_G):
        return False
    return True

# Perform the transition and return the new state
def transition(state, item):
    F, W, G, C = state
    new_F = 'W' if F == 'E' else 'E'
    new_W, new_G, new_C = W, G, C
    if item == 'W':
        new_W = new_F
    elif item == 'G':
        new_G = new_F
    elif item == 'C':
        new_C = new_F
    return (new_F, new_W, new_G, new_C)

# Generate successors for a given state
def successors(state):
    next_states = []
    for item in ['W', 'G', 'C', '']:
        if is_safe_transition(state, item):
            next_state = transition(state, item)
            next_states.append(next_state)
    return next_states

# Depth-First Search Algorithm
def dfs_search(start, goal):
    stack = [(start, [start])]
    #to stop the stack growing too large
    visited = set([start])
    while stack:
        (state, path) = stack.pop()
        for next_state in successors(state):
            if next_state in visited:
                continue
            visited.add(next_state)
            if next_state == goal:
                return path + [next_state]
            stack.append((next_state, path + [next_state]))


# A* Search Algorithm
def a_star_search(start, goal):
    heap = [(heuristic(start), start, [start])]
    while heap:
        (cost, state, path) = heapq.heappop(heap)
        for next_state in successors(state):
            new_cost = cost - heuristic(state) + heuristic(next_state)
            if next_state == goal:
                return path + [next_state]
            heapq.heappush(heap, (new_cost, next_state, path + [next_state]))

# Main Function
if __name__ == '__main__':
    start = ('E', 'E', 'E', 'E')
    goal = ('W', 'W', 'W', 'W')

    dfs_path = dfs_search(start, goal)
    print('DFS Path:', dfs_path)

    a_star_path = a_star_search(start, goal)
    print('A* Path:', a_star_path)
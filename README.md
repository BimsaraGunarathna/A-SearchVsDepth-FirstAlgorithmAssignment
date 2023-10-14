# Farmer, Wolf, Goat and Cabbage Problem

## Step 1: Problem Analysis and Design

### 1. Representation of the State

A state can be represented as a tuple `(F, W, G, C)`, where each element can be either 'E' (East) or 'W' (West). For example, the initial state can be `('E', 'E', 'E', 'E')` and the goal state can be `('W', 'W', 'W', 'W').

### 2. Representation of the State Space

The state space can be represented as a tree, where each node is a state. The tree should be at least 8 levels deep to meet the assignment requirements.

### 3. Design of the Heuristic Evaluation Function in A* Algorithm

The heuristic function can be the count of items (excluding the farmer) that are still on the east side. This is admissible because moving each item to the west side takes at least one action.

```python
def heuristic(state):
    return sum([1 for item in state[1:] if item == 'E'])
```

### 4. Strategy to Avoid Unsafe States

Unsafe states occur when:

- The wolf and the goat are on the same side and the farmer is on the opposite side.
- The goat and the cabbage are on the same side and the farmer is on the opposite side.

We can avoid these states by not generating them in the first place.

## Step 2: Coding

### Depth-First Search Algorithm

```python
def dfs_search(start, goal):
    stack = [(start, [start])]
    while stack:
        (state, path) = stack.pop()
        for next_state in successors(state):
            if next_state == goal:
                return path + [next_state]
            stack.append((next_state, path + [next_state]))
```

### A* Search Algorithm

```python
import heapq

def a_star_search(start, goal):
    heap = [(heuristic(start), start, [start])]
    while heap:
        (cost, state, path) = heapq.heappop(heap)
        for next_state in successors(state):
            new_cost = cost - heuristic(state) + heuristic(next_state)
            if next_state == goal:
                return path + [next_state]
            heapq.heappush(heap, (new_cost, next_state, path + [next_state]))
```

### Successor Function

```python
def successors(state):
    F, W, G, C = state
    next_states = []
    for item in ['W', 'G', 'C', '']:
        if is_safe_transition(state, item):
            next_state = transition(state, item)
            next_states.append(next_state)
    return next_states
```

### Main Function

```python
if __name__ == "__main__":
    start = ('E', 'E', 'E', 'E')
    goal = ('W', 'W', 'W', 'W')

    dfs_path = dfs_search(start, goal)
    print("DFS Path:", dfs_path)

    a_star_path = a_star_search(start, goal)
    print("A* Path:", a_star_path)
```
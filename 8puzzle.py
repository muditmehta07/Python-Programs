import heapq

neighbors = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def manhattan(state, goal_pos):
    distance = 0

    for i, val in enumerate(state):
        if val != 0:
            goal_index = goal_pos[val]
            distance += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)

    return distance

def astar(start, goal):
    goal_pos = {val:i for i, val in enumerate(goal)}
    open_set = [(manhattan(start, goal_pos), 0, start, [])]
    closed_set = set()

    while open_set:
        _, g, state, path = heapq.heappop(open_set)
        if state in closed_set:
            continue

        closed_set.add(state)

        if state == goal:
            return path + [state]
        
        zero = state.index(0)

        for neighbor in neighbors[zero]:
            new_state = list(state)
            new_state[zero], new_state[neighbor] = new_state[neighbor], new_state[zero]
            new_state_tuple = tuple(new_state)

            if new_state_tuple not in closed_set:
                h = manhattan(new_state_tuple, goal_pos)
                heapq.heappush(open_set, (g + 1 + h, g + 1, new_state_tuple, path + [state]))
                
    return None

def print_state(state):
    for i in range(3):
        print(state[i*3:(i+1)*3])
    print()

if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    solution = astar(start, goal)

    if solution:
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
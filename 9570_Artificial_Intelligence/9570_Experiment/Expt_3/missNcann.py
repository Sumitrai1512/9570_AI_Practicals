class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if (3 - self.missionaries) < (3 - self.cannibals) and (3 - self.missionaries) > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __repr__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {'left' if self.boat == 1 else 'right'}"


# Actions represented using vector subtraction/addition
ACTIONS = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]


def successors(state):
    moves = []
    for action in ACTIONS:
        if state.boat == 1:
            new_state = State(state.missionaries - action[0], state.cannibals - action[1], 0)
        else:
            new_state = State(state.missionaries + action[0], state.cannibals + action[1], 1)
        if new_state.is_valid():
            moves.append(new_state)
    return moves


def dfs(start_state, visited):
    stack = [(start_state, [start_state])]
    while stack:
        (state, path) = stack.pop()
        if state.is_goal():
            return path
        if state not in visited:
            visited.add(state)
            for successor in successors(state):
                if successor not in visited:
                    stack.append((successor, path + [successor]))
    return None


def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")


def main():
    initial_state = State(3, 3, 1)
    visited = set()
    solution = dfs(initial_state, visited)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

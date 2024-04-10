def dfs_water_jug(capacity_a, capacity_b, target):
    stack = [(0, 0, [])]  # (current state A, current state B, path)
    visited = set()

    while stack:
        current_state_a, current_state_b, path = stack.pop()

        if (current_state_a, current_state_b) == target:
            return path

        if (current_state_a, current_state_b) in visited:
            continue

        visited.add((current_state_a, current_state_b))

        # Fill jug A
        stack.append((capacity_a, current_state_b, path + [(current_state_a, current_state_b, 'Fill A')]))

        # Fill jug B
        stack.append((current_state_a, capacity_b, path + [(current_state_a, current_state_b, 'Fill B')]))

        # Empty jug A
        stack.append((0, current_state_b, path + [(current_state_a, current_state_b, 'Empty A')]))

        # Empty jug B
        stack.append((current_state_a, 0, path + [(current_state_a, current_state_b, 'Empty B')]))

        # Pour water from jug A to jug B
        pour_amount = min(current_state_a, capacity_b - current_state_b)
        stack.append((current_state_a - pour_amount, current_state_b + pour_amount,
                      path + [(current_state_a, current_state_b, 'Pour A to B')]))

        # Pour water from jug B to jug A
        pour_amount = min(current_state_b, capacity_a - current_state_a)
        stack.append((current_state_a + pour_amount, current_state_b - pour_amount,
                      path + [(current_state_a, current_state_b, 'Pour B to A')]))

    return None  # No solution found


# Example usage:
capacity_a = 4
capacity_b = 3
target_amount = (2, 0)

result = dfs_water_jug(capacity_a, capacity_b, target_amount)

if result:
    print(f"Solution found in {len(result)} steps:")
    for step in result:
        print(f"Step: {step[-1]}, Current State: Jug A = {step[0]}, Jug B = {step[1]}")
else:
    print("No solution found.")
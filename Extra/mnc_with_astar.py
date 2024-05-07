from queue import PriorityQueue

def heuristic(state):
    m_left, c_left, b_pos, m_right, c_right = state
    return (m_left+c_left-2)//2 +(m_right+c_right-2)//2


def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right >3  or c_right > 3:
        return False
    if (c_left>m_left>0) or (c_right>m_right>0):
        return False
    return True

def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if b_pos == "left":
        moves=[(2,0),(0,2),(1,1),(1,0),(0,1)]
        #This is basically 2 Ms 0 Cs -> So it represents boat mai kitne log aur kon kon jaah raha hai
        next_states = [(m_left-m, c_left-c, 'right', m_right+m, c_right+c) for m, c in moves]

    else:
        moves = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
        next_states=[(m_left+m,c_left+c,'left',m_right-m,c_right-c) for m,c in moves]

    return [state for state in next_states if is_valid(state)]


def a_star(start_state):
    frontier = PriorityQueue()
    frontier.put((heuristic(start_state),[start_state]))
    #AISE STORE HOGA
    # (10, [(3, 3, 'left', 0, 0)])    
    explored=set()

    while not frontier.empty():
        #taking the state from the frontier queue
        path=frontier.get()[1]
        # Curent Path -> [(3, 3, 'left', 0, 0),(3, 2, 'right', 0, 1)], So we need to continue to work with the last state, which will be our next "Current State"
        current_state=path[-1]

        if current_state == (0, 0, 'right', 3, 3):
            return path
        
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_path=path+[next_state]
                #DEMONSTRATION OF THE STEP
                # path =[(3, 3, 'left', 0, 0)]
                # next_state=(3, 2, 'right', 0, 1)
                # new_path = path+[next_state]
                # new_path = [(3, 3, 'left', 0, 0),(3, 2, 'right', 0, 1)]  
                frontier.put((len(new_path)+heuristic(next_state),new_path))
                explored.add(next_state)

    return None


path = a_star((3, 3, 'left', 0, 0))
# print(paths)
for state in path:
    m_left, c_left, b_pos, m_right, c_right = state
    print(
        f"Left Side: {m_left}Ms & {c_left}Cs \t Boat:{b_pos} \t Right Side: {m_right}Ms & {c_right}Cs")





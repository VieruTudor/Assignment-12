def difference(value1, value2):
    return abs(value1 - value2)


def isConflict(value1, value2):
    if difference(value1, value2) == 1:
        return True
    return False


'''
   initial perm : 1 2 3 4 5
      good perm : 1 4 2 5 3
'''


def backtrackingCondition(stack, stackTop):
    for index in range(0, stackTop):
        numberOfNeighbours = stackTop - index - 1
        # condition for permutations
        if stack[stackTop] == stack[index]:
            return False
        # if they are in conflict
        if isConflict(stack[stackTop], stack[index]) is True:
            # if they are one next to each other
            if numberOfNeighbours == 0:
                return False
            # if they are too far apart
            if numberOfNeighbours >= 3:
                return False
            # if they have the good distance but the splitting neighbours are in conflict with them or one with each
            # other
            for index2 in range(index, stackTop):
                if isConflict(stack[index2], stack[index2 + 1]):
                    return False
    return True


def recursiveBacktracking(stack, stackTop, chairs):
    for index in range(0, chairs, 1):
        # trying a candidate
        stack[stackTop] = index
        # checking if the solution is good until that point
        if backtrackingCondition(stack, stackTop):
            # check if the stack is full, if so, we got a solution
            if stackTop == chairs - 1:
                print([_ + 1 for _ in stack])
            else:
                # try again
                recursiveBacktracking(stack, stackTop + 1, chairs)


def iterativeBacktracking(stack, stackTop, chairs):
    # initialise top of the stack with the minimum value - 1
    stack[stackTop] = -1
    # as long as the stack is not empty
    while stackTop > -1:
        # we don't have a candidate yet
        candidate = False
        # we don't have a candidate and the stack is not full
        while not candidate and stack[stackTop] < chairs - 1:
            # we move on with the top of the stack
            stack[stackTop] += 1
            # checking if the solution is good so far
            candidate = backtrackingCondition(stack, stackTop)
        # if we still haven't found a candidate, then we are going on a "dead" branch of the tree, so we move back
        if candidate is False:
            stackTop -= 1
        else:
            if stackTop == chairs - 1:
                print([_ + 1 for _ in stack])
            # we found a candidate, but there is room for more
            else:
                stackTop += 1
                stack[stackTop] = -1


def main():
    stackTop = 0
    chairs = int(input("Number of chairs : "))
    stack = [0] * chairs
    print("Type of backtracking")
    print("1.Recursive\n"
          "2.Iterative\n")
    backType = input(">")
    if backType == "1":
        recursiveBacktracking(stack, stackTop, chairs)
    if backType == "2":
        iterativeBacktracking(stack, stackTop, chairs)


main()

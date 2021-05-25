# Write a program that writes a given permutation as a product of disjoint cycles (and of transpositions).


# Gets inputPermutations
# Creates mappedPermutations
# Return list of cycles as a whole list
def ReturnDisjointCyclesAsList(inputPermutations):
    mappedPermutations = dict()
    resultDisjointCycles = list()

    for i in (range(len(inputPermutations))):
        mappedPermutations[i + 1] = inputPermutations[i]

    # Main Logic
    while mappedPermutations != {}:
        pastValue = list(mappedPermutations.keys())[0] # Get first index for mapped permutation
        tempList = [pastValue] # List for each cycle

        while True:
            actualValue = mappedPermutations[pastValue]
            del mappedPermutations[pastValue] # Delete mapped permutation (1 -> 5) after 5 is actualValue

            # For ex. 1 -> 5 -> 4 -> 1 or 2 -> 2
            if tempList[0] == actualValue or pastValue == actualValue:
                break 
            else:
                tempList.append(actualValue)
                pastValue = actualValue
        
        resultDisjointCycles.append(tempList)
    # Return
    return resultDisjointCycles


# Return Transpositions of Cycle (> 2)
def ReturnTranspositionOfOneCycleAsList(cycle):
    resultTranspositions = []
    revCycle = cycle[::-1]
    
    for i in range(1, len(revCycle)):
        couple = [revCycle[i-1], revCycle[i]]
        resultTranspositions.append(couple)
            
    return resultTranspositions


# Get disjointCycles
# Returns 2-cycles (a.k.a transposition)
def ReturnTranspositionCyclesAsList(disjointCycles):
    resultTranspositionedCycles = []

    for cycle in disjointCycles:
        if len(cycle) > 2:
            transpositionList = ReturnTranspositionOfOneCycleAsList(cycle)
            for i in transpositionList:
                resultTranspositionedCycles.append(i)

        else:
            resultTranspositionedCycles.append(cycle) 

    return resultTranspositionedCycles



# Return: List of Cycles except 1-cycles
def ReturnCyclesExceptOneCycle(resultCycles):
    return [cycle for cycle in resultCycles if len(cycle) > 1]



# Gets list of cycles and 
# Returns them like we write in paper
def ReturnCyclesAsString(resultCycles):
    resultString = ""

    for i in resultCycles:
        resultString += f"({', '.join(list(map(str, (i))))}) "
    
    return resultString



# My Driver
if __name__ == '__main__':
    inputPermutations = list(map(int, input().split()))
    print("---------------------------------------------\n")

    disjointCycles = ReturnDisjointCyclesAsList(inputPermutations)
    print("Disjoint cycles:", ReturnCyclesAsString(disjointCycles))

    transpositionCycles = ReturnTranspositionCyclesAsList(disjointCycles)
    if disjointCycles != transpositionCycles:
        print("Transpositions:", ReturnCyclesAsString(transpositionCycles))
    else:
        print("We don't need to show cycle as a product of transpositions")


    # Other Version of Printing
    print("---------------------------------------------\n")

    disjointCycles = ReturnCyclesExceptOneCycle(ReturnDisjointCyclesAsList(inputPermutations))
    print("Disjoint cycles:", ReturnCyclesAsString(disjointCycles))

    transpositionCycles = ReturnCyclesExceptOneCycle(ReturnTranspositionCyclesAsList(disjointCycles))
    if disjointCycles != transpositionCycles:
        print("Transpositions:", ReturnCyclesAsString(transpositionCycles))
    else:
        print("We don't need to show cycle as a product of transpositions")


    print("---------------------------------------------\n")
    if len(transpositionCycles) % 2:
        print("This permutation is ODD")
    else:
        print("This permutation is EVEN")


    print("---------------------------------------------\n")

    input("Press any key to EXIT:")
# Write a program that writes a given permutation as a product of disjoint cycles (and of transpositions).

def ReturnDisjointCyclesAsList(inputPermutations):
    mappedPermutations = dict()
    resultDisjointCycles = list()

    for i in (range(len(inputPermutations))):
        mappedPermutations[i + 1] = inputPermutations[i]

    while mappedPermutations != {}:
        pastValue = list(mappedPermutations.keys())[0] 
        tempList = [pastValue] 

        while True:
            actualValue = mappedPermutations[pastValue]
            del mappedPermutations[pastValue] 

            if tempList[0] == actualValue or pastValue == actualValue:
                break 
            else:
                tempList.append(actualValue)
                pastValue = actualValue
        
        resultDisjointCycles.append(tempList)
    return resultDisjointCycles


def ReturnTranspositionOfOneCycleAsList(cycle):
    resultTranspositions = []
    revCycle = cycle[::-1]
    
    for i in range(1, len(revCycle)):
        couple = [revCycle[i-1], revCycle[i]]
        resultTranspositions.append(couple)
            
    return resultTranspositions


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



def ReturnCyclesExceptOneCycle(resultCycles):
    return [cycle for cycle in resultCycles if len(cycle) > 1]



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
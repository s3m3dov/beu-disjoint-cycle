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



# Get disjointCycles
# Returns 2-cycles (a.k.a transposition)
def ReturnTranspositionCyclesAsList(disjointCycles):
    return None



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

    disjointCycles = ReturnDisjointCyclesAsList(inputPermutations)
    transpositionCycles = ReturnTranspositionCyclesAsList(disjointCycles)

    print("Disjoint cycles:", ReturnCyclesAsString(disjointCycles))
    print("Transpositions:", ReturnCyclesAsString(transpositionCycles))
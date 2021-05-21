"""
Write a program that writes a given permutation as a product of
disjoint cycles (and of transpositions).
"""
import  time

if __name__ == '__main__':
    inp_permutation = list(map(int, input().split()))
    mappedPermutation = {}
    my_result = []


    for i in (range(len(inp_permutation))):
        mappedPermutation[i + 1] = inp_permutation[i]
    
    # print(list(mappedPermutation.keys())[0])
    

    while mappedPermutation != {}:
        pastValue = list(mappedPermutation.keys())[0]
        temp_list = [pastValue]

        while True:
            actualValue = mappedPermutation[pastValue]
            del mappedPermutation[pastValue]


            # Break
            if temp_list[0] == actualValue or pastValue == actualValue:
                break 

            else:
                pastValue = actualValue
                temp_list.append(actualValue)


        my_result.append(temp_list)
        #print(my_result, mappedPermutation)
        #time.sleep(3)

    # Finish Part
    if len(my_result) == 1:
        print("Single cycle: (", ", ".join(list(map(str, (my_result[0])))), ")", sep="")
        
    else:
        print("Disjoint cycles:", end=' ')

        for i in my_result:
            print("(", ", ".join(list(map(str, (i)))), ")", sep='', end=' ')

        print()
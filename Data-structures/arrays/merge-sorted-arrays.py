array_1 = [0, 3, 4];
array_2 = [0, 4, 6, 30];
# a=[1,3,4,6,20]
# b=[2,3,4,5,6,9,11,76]

def merge_sorted_array(arr1, arr2):

    if (len(arr1) == 0 or len(arr2) == 0):
        return arr1 + arr2 

    result= []
    i=0
    j=0
    
    while ((i < len(arr1)) and (j < len(arr2))):
        print(arr1[i], arr2[j])
        if arr1[i] <= arr2[j]:
            if arr1[i] not in result: # Item added only when not in the list
                result.append(arr1[i])
            i += 1 
        elif arr2[j] < arr1[i]:
            if arr2[j] not in result: # Item added only when not in the list
                result.append(arr2[j])
            j += 1

    # For handling remaining numbers if in the result (To avoid repetition of numbers)
    arr1_remainder = arr1[i:]
    arr2_remainder = arr2[j:]

    if len(arr1_remainder) > 0:
        for i in arr1_remainder:
            if i not in result:
                result.append(i)

    if len(arr2_remainder) > 0: 
        for i in arr2_remainder:
            if i not in result:
                result.append(i)

    return result


print(merge_sorted_array(array_1, array_2))
# print(merge_sorted_array(a, b))


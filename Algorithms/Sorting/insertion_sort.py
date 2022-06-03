arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0] 
arr1 = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

# def insertion_sort(arr):
#     length = len(arr)
#     i = 1 
#     end_sorted_array = arr[0]

#     while (i < length):
#         if (arr[i] < end_sorted_array):
#             x = arr.pop(i)

#             for j in range(0, i):
#                 if (x < arr[j]):
#                     arr.insert(j, x)
#                     break 

#         end_sorted_array = arr[i] 
#         i += 1 

#     return arr 


# print(insertion_sort(arr))
# print(insertion_sort(arr1))

# def insertion_sort1(arr):

#     array_length = len(arr)

#     for i in range(1, array_length):

#         value = arr[i]
#         hole = i 

#         while ((hole > 0) and (arr[hole - 1] > value)):
#             # SWAP 
#             arr[hole] = arr[hole - 1] 
#             hole = hole - 1 
        
#         arr[hole] = value 

#     return arr 

# print(arr)
# print(insertion_sort1(arr))
# print(arr1)
# print(insertion_sort1(arr1))

# INTUITIVE SOLUTION 

def insertion_sort(arr):

    array_length = len(arr)
    i = 1 
    end_sorted_array = arr[0] 

    print(array_length)
    while i < array_length:
        if (arr[i] < end_sorted_array):
            x = arr.pop(i) 

            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break 

        end_sorted_array = arr[i] 

        i += 1

        print(arr)

    return arr 

print(insertion_sort(arr))

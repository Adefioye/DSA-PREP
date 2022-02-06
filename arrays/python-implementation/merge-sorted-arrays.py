array_1 = [0, 3, 4];
array_2 = [0, 4, 6, 30];

# def merge_sorted_arrays(array_1, array_2):
#     merged_array = []
#     array_1_item = array_1[0]
#     array_2_item = array_2[0]
#     i = 0
#     j = 0 
#     while (array_1_item | array_2_item):
#         print(array_1_item, array_2_item)
#         if ((not array_2_item) | (array_1_item < array_2_item)):
#             merged_array.append(array_1_item)
#             i += 1
#             try:
#                 array_1_item = array_1[i]
#             except:
#                 array_1_item = False
#         else:
#             merged_array.append(array_2_item)
#             j += 1 
#             try:
#                 array_2_item = array_2[j]
#             except:
#                 array_2_item = False

#     return merged_array

# print(merge_sorted_arrays(array_1, array_2))
# print(False | False)


# The below function works provided that none of the inputs is 0
def merge_sorted_arrays_2(array_1, array_2):
    merged_array = []
    array_1_item = array_1[0]
    array_2_item = array_2[0]
    i = 0
    j = 0 

    if (max(array_1) < max(array_2)):
        while (array_1_item | array_2_item):
            print(array_1_item, array_2_item)

            if (((not (array_1_item)) | (array_1_item == 0)) | (array_2_item < array_1_item)):
                merged_array.append(array_2_item)
                j += 1
                try:
                    array_2_item = array_2[j]
                except:
                    array_2_item = False
            else:
                merged_array.append(array_1_item)
                i += 1 
                try:
                    array_1_item = array_1[i]
                except:
                    array_1_item = False
    else:
        while (array_1_item | array_2_item):
            print(array_1_item, array_2_item)
            if (((not (array_2_item)) | (array_2_item == 0)) | (array_1_item < array_2_item)):
                merged_array.append(array_1_item)
                i += 1
                try:
                    array_1_item = array_1[i]
                except:
                    array_1_item = False
            else:
                merged_array.append(array_2_item)
                j += 1 
                try:
                    array_2_item = array_2[j]
                except:
                    array_2_item = False

    return merged_array



print(merge_sorted_arrays_2(array_1, array_2))
# print(min(array_1))
# print(min(array_2))






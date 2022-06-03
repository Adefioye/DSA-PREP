# 
arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# def bubble_sort(arr):
#     length = len(arr)
#     for i in range(length - 1):
#         for j in range(length - 1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j + 1]
#                 arr[j + 1] = arr[j]
#                 arr[j] = temp 
    
#     return arr 


# print(bubble_sort(arr))

def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                # SWAP 
                temp = arr[j + 1] 
                arr[j + 1] = arr[j] 
                arr[j] = temp 
    
    return arr 

print(bubble_sort(arr))

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0] 

def merge(left, right):

    result = []
    left_length = len(left) 
    right_length = len(right) 
    left_index = 0 
    right_index = 0

    while((left_index < left_length) and (right_index < right_length)):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1 
    
    while left_index < left_length:
        result.append(left[left_index])
        left_index += 1 

    while right_index < right_length: 
        result.append(right[right_index])
        right_index += 1 

    return result

def merge_sort(array):
    array_length = len(array)

    if array_length < 2:
        return array

    mid = array_length // 2
    left = array[:mid] 
    right = array[mid:]

    print("Left", left) 
    print("Right", right)

    return merge(merge_sort(left), merge_sort(right)) 


print(merge_sort(arr))


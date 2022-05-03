arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(arr):
    length = len(arr)
    
    for i in range(length):
        min = i 
        temp = arr[i]
        for j in range(i + 1, length):
            if (arr[j] < arr[min]):
                min = j

        arr[i] = arr[min]
        arr[min] = temp 

    return arr 


print(selection_sort(arr))
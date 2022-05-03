arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0] 
arr1 = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

def insertion_sort(arr):
    length = len(arr)
    i = 1 
    end_sorted_array = arr[0]

    while (i < length):
        if (arr[i] < end_sorted_array):
            x = arr.pop(i)

            for j in range(0, i):
                if (x < arr[j]):
                    arr.insert(j, x)
                    break 

        end_sorted_array = arr[i] 
        i += 1 

    return arr 


print(insertion_sort(arr))
print(insertion_sort(arr1))
num1 = [2, 4, 1, 6, 8, 5, 3, 7]

def mergeSort(A):

    aLen = len(A)

    if aLen < 2:
        return 
    
    mid = aLen // 2 
    left = A[:mid]
    right = A[mid:]

    mergeSort(left)
    mergeSort(right)
    merge(left, right, A)

    return A 

def merge(left, right, A):
    
    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):

        if left[l] <= right[r]:
            A[k] = left[l]
            l += 1
        else:
            A[k] = right[r]
            r += 1
        
        k += 1

        print(k)

    while l < len(left):
        A[k] = left[l]
        l += 1
        k += 1

        print(k)

    while r < len(right):
        A[k] = right[r]
        r += 1
        k += 1

        print(k)
    

print(mergeSort(num1))
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if len(arrA) == 0:
        return arrA
    elif len(arrB) == 0:
        return arrB

    indexA = indexB = 0
    merged_arr = []
    list_len_target = len(arrA) + len(arrB)
    while len(merged_arr) < list_len_target:
        if arrA[indexA] <= arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1

        if indexB == len(arrB):
            merged_arr += arrA[indexA:]
        elif indexA == len(arrA):
            merged_arr += arrB[indexB:]
    return merged_arr


def split(arr):
    arr_len = len(arr)
    midpoint = arr_len // 2
    return arr[:midpoint], arr[midpoint:]

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        left, right = split(arr)
        return merge(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here
#

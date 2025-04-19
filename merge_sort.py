def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = (0+len(arr)) // 2

    arr1 = merge(arr[:mid])
    arr2 = merge(arr[mid:])

    return merge_sort(arr1, arr2)


def merge_sort(arr1, arr2):
    i = 0
    j = 0
    arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i +=1
        else:
            arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    return arr




arr = [2,1,3,4,5,1]

print(merge(arr))
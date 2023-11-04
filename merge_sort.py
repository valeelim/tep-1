
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    
    ptr1, ptr2 = 0, 0
    while ptr1 < len(left) and ptr2 < len(right):
        if left[ptr1] < right[ptr2]:
            result.append(left[ptr1])
            ptr1 += 1
        else:
            result.append(right[ptr2])
            ptr2 += 1
        
    while ptr1 < len(left):
        result.append(left[ptr1])
        ptr1 += 1

    while ptr2 < len(right):
        result.append(right[ptr2])
        ptr2  += 1
    
    return result


if __name__ == '__main__':
    test = [1, 5, 6, 2, 3, 5, 2, 10]
    assert sorted(test) == merge_sort(test)
    

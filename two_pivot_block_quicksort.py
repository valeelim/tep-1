import sys
import os

BLOCK_SIZE = 64

def partition(arr, l, r):
    n = r - l + 1
    if n <= 1:
        return (l, r)
    if arr[l] > arr[r]:
        arr[l], arr[r] = arr[r], arr[l]

    p, q = arr[l], arr[r]
    block = [0 for _ in range(BLOCK_SIZE)]
    i, j, k = 1+l, 1+l, 1
    nlp, nlq = 0, 0
    while k < n-1:
        t = min(BLOCK_SIZE, n - k - 1)
        for c in range(t):
            block[nlq] = c
            nlq = nlq + (q >= arr[k + c + l])

        for c in range(nlq):
            arr[j + c], arr[k + block[c] + l] = arr[k + block[c] + l], arr[j + c]

        k = k + t
        for c in range(nlq):
            block[nlp] = c
            nlp = nlp + (p > arr[j + c])

        for c in range(nlp):
            arr[i], arr[j + block[c]] = arr[j + block[c]], arr[i]
            i += 1
        
        j += nlq
        nlp, nlq = 0, 0

    arr[i-1], arr[l] = arr[l], arr[i-1]
    arr[j], arr[r] = arr[r], arr[j]

    return (i-1, j)

def two_pivot_block_lomuto(arr, l=None, r=None):
    if l is None:
        l, r = 0, len(arr)-1
    
    rec_stack = [(l, r)]

    while len(rec_stack):
        l, r = rec_stack.pop()
        i, j = partition(arr, l, r)

        if l < i-1:
            rec_stack.append((l, i-1))
        if i+1 < j-1:
            rec_stack.append((i+1, j-1))
        if j+1 < r:
            rec_stack.append((j+1, r))
    
    return arr

# Segmentation Fault (Recursion memory overload)
# ==============================
# def two_pivot_block_lomuto(arr, l=None, r=None):
#     if l is None:
#         l, r = 0, len(arr)-1
    
#     if l < r:
#         i, j = partition(arr, l, r)
#         two_pivot_block_lomuto(arr, l, i-1)
#         two_pivot_block_lomuto(arr, i+1, j-1)
#         two_pivot_block_lomuto(arr, j+1, r)
    

if __name__ == '__main__':
    sys.setrecursionlimit(2**17)

    with open(os.path.join('dataset', '2^9.txt'), 'r') as f:
        test = [int(num) for num in f.read().split('\n')]
    
    assert sorted(test) == two_pivot_block_lomuto(test[:])
    
    
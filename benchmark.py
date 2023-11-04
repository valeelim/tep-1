import os
import sys

from two_pivot_block_quicksort import two_pivot_block_lomuto
from merge_sort import merge_sort
from util import log_exec_time
from util import profile_memory

def is_sorted(arr, asc=True):
    if asc:
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))


@log_exec_time
def test_mergesort(arr):
    return merge_sort(arr)

@log_exec_time
def test_two_pivot(arr):
    return two_pivot_block_lomuto(arr)

# separate memory and time benchmark
@profile_memory
def mem_test_mergesort(arr):
    return merge_sort(arr)

@profile_memory
def mem_test_two_pivot(arr):
    return  two_pivot_block_lomuto(arr)
        
if __name__ == '__main__':
    sys.setrecursionlimit(2**17)

    dataset_dir = 'dataset'
    if not os.path.exists(dataset_dir):
        sys.exit('Dataset directory does not exist.')

    
    for file_name in os.listdir(dataset_dir):
        with open(os.path.join(dataset_dir, file_name), 'r') as f:
            data = [int(num) for num in f.read().split('\n')]
        
        print(f'Running {file_name}\n{"=" * 30}')

        # assert is_sorted(test_two_pivot(data[:]))
        # assert is_sorted(test_mergesort(data[:]))

        print (f'Memory usage:')
        mem_test_mergesort(data[:])
        mem_test_two_pivot(data[:])
        
    


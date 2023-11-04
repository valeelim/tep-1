import os
import sys

from two_pivot_block_quicksort import two_pivot_block_lomuto
from merge_sort import merge_sort
from timeit import default_timer as timer
from functools import wraps
from memory_profiler import memory_usage

def is_sorted(arr, asc=True):
    if asc:
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    return all(arr[i] >= arr[i+1] for i in range(len(arr)-1))

def profile_memory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def target():
            return func(*args, **kwargs)
        
        mem_usage, retval = memory_usage(target, interval=.1, timeout=1, retval=True, max_usage=True)
        print(f">{func.__name__}'s memory usage: {mem_usage} MiB.")
        return retval
    return wrapper


def log_exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f'>{func.__name__} took {(end - start) * 1000} miliseconds.')
        return result
    return wrapper

@log_exec_time
@profile_memory
def test_mergesort(arr):
    return merge_sort(arr)

@log_exec_time
@profile_memory
def test_two_pivot(arr):
    return two_pivot_block_lomuto(arr)
        
if __name__ == '__main__':
    sys.setrecursionlimit(2**17)

    dataset_dir = 'dataset'
    if not os.path.exists(dataset_dir):
        sys.exit('Dataset directory does not exist.')

    
    for file_name in os.listdir(dataset_dir):
        with open(os.path.join(dataset_dir, file_name), 'r') as f:
            data = [int(num) for num in f.read().split('\n')]
        
        print(f'Running {file_name}\n{"=" * 30}')

        assert is_sorted(test_two_pivot(data[:]))
        assert is_sorted(test_mergesort(data[:]))
        print()

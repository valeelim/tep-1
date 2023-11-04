
from timeit import default_timer as timer
from functools import wraps
from memory_profiler import memory_usage

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
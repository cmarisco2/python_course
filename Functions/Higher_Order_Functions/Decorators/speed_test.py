# define speed test using a decorator

from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = fn(*args, **kwargs)
        stop_time = time() - start_time
        print(f'using {fn.__name__}')
        print(f'Total duration was: {stop_time}')
        return res
    return wrapper


@speed_test
def sum_nums_list(num):
    return sum([x for x in range(num)])


@speed_test
def sum_nums_gen(num):
    return sum(x for x in range(num))


print(sum_nums_list(100000000))
print(sum_nums_gen(100000000))

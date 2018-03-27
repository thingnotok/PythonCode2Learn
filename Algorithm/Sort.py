# Sort

"""
def pairwise(it):
    it = iter(it)
    while True:
        yeild next(it), next(it)
"""

bench_list = [1, 3, 2, 4, 1, 5]

#_list = bench_list



def bubble_sort(_list):
    # my implementation for bubble sort
    size = len(_list)
    for run in range(1, size+1):
        for idx in range(0, size-run):
            if _list[idx] > _list[idx+1]:
                _list[idx], _list[idx+1] = _list[idx+1], _list[idx]
    return _list



def select_sort(_list):
    result = []
    tmp = _list
    for run in range(len(_list)):
        argMin = 0
        Min = tmp[0]
        for idx, element in enumerate(tmp):
             if element < Min:
                 argMin = idx
                 Min = element
        result.append(Min)
        tmp[argMin] = tmp[0]
        tmp = tmp[1:]
    return result

"""
import random
for i in range(10):
    bench_list = random.sample(range(10000), 1000)
    print(sum(bench_list))
    print(bubble_sort(bench_list) == sorted(bench_list))


import timeit
t = timeit.Timer('bubble_sort(bench_list)', 
                 setup='from __main__ import bubble_sort, bench_list').timeit(100)
t_cpy = timeit.Timer('sorted(bench_list)',
                      setup='from __main__ import bench_list').timeit(100)
print(t, t_cpy)
"""

print(select_sort(bench_list))
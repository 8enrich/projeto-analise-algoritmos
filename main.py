from random import randint
from time import time
import json

def merge_index(arr, start1, end1, start2, end2):
    i, k = start1, start2
    result = []
    while i <= end1 and k <= end2:
        if arr[i] < arr[k]:
            result.append(arr[i])
            i += 1
            continue
        result.append(arr[k])
        k += 1
    result.extend(arr[i:end1 + 1])
    result.extend(arr[k:end2 + 1])
    for offset, val in enumerate(result):
        arr[start1 + offset] = val
    return arr

def mergesort_index(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1 
    if i < j:
        h = (i + j)//2
        mergesort_index(arr, i, h)
        mergesort_index(arr, h + 1, j)
        return merge_index(arr, i, h, h + 1, j)

def merge(arr1, arr2):
    i = k = 0
    result = []
    while i < len(arr1) and k < len(arr2):
        if arr1[i] < arr2[k]:
            result.append(arr1[i])
            i += 1
            continue
        result.append(arr2[k])
        k += 1
    result.extend(arr1[i:])
    result.extend(arr2[k:])
    return result

def mergesort_slice(arr):
    n = len(arr)
    if n < 2:
        return arr
    h = n//2
    arr1 = mergesort_slice(arr[:h])
    arr2 = mergesort_slice(arr[h:])
    return merge(arr1, arr2)

def get_merge_runtime(func, arr):
    start = time()
    func(arr)
    end = time()
    return end - start

def test():
    k = randint(100, 200)
    m = randint(10, 20)
    sizes = [10 + i * ((10000 - 10) // (k - 1)) for i in range(k)]
    test_cases = []
    for n in sizes:
        slice_time_sum = 0
        index_time_sum = 0
        for _ in range(m):
            arr = [randint(-2 * n, 2 * n) for _ in range(n)]
            slice_time_sum += get_merge_runtime(mergesort_slice, arr)
            index_time_sum += get_merge_runtime(mergesort_index, arr)
        test_cases.append({
            "SIZE": n,
            "SLICE_MEAN_TIME": slice_time_sum/m,
            "INDEX_MEAN_TIME": index_time_sum/m,
            "DIFF": f"{((index_time_sum - slice_time_sum)*1000)/m:.2f} ms"
        })
    result = {
        "test_cases": test_cases,
        "k": k,
        "m": m
    }  
    with open("results/test.json", "w") as file:
        json.dump(result, file, indent=2)

test()

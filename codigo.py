def quickFilter(arr: list[int]):
    if(len(arr) < 2):
        return arr
    else:
        pivot: int = arr[0]
        major = list(filter(lambda x: x > pivot, arr))
        minor = list(filter(lambda x: x < pivot, arr))
        return quickFilter(minor) + [pivot] + quickFilter(major)
    
arr: list[int] = [99, 98, 0, -1, 8]
response: list[int] = quickFilter(arr)
print(response)
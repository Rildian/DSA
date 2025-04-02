def binarySearch(array: list, n: int) -> int:
    lowest = 0
    highest = len(array) 

    while lowest < highest:
        mid = int(lowest + ((highest-lowest)/2))
        print(f"O mid tá na posição: {mid}")

        if n == array[mid]:
            return mid 
        elif array[mid] < n:
            lowest = mid + 1
        else:
            highest = mid 
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(binarySearch(array, 10))
array = [2, 5, 10, 22, 45, 56, 61, 72, 88, 95]
target = 5
def binary_search(arr,target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr)//2
        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] > target:
                return binary_search(arr[:midpoint], target)
            else:
                return binary_search(arr[midpoint+1:], target)
print(binary_search(array,target))
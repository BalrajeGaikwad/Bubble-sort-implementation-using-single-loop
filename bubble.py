"""def bubble(num):
    length=len(num)
    for i in range(length):
        for j in range(0,length-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]

num=[2,4,1,5,4,2,1]
print("unsorted numbers :-",num)

bubble(num)
print("sorted numbers :-",num)"""



#Stops early if the list is already sorted.

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Exit early if no swaps occurred in the last pass
arr=[2,4,1,5,4,2,1]
optimized_bubble_sort(arr)
print(arr)



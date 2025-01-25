"""arr = [5, 3, 8, 6, 2, 7, 4, 1]

i = 0  # Index for the loop
while i < len(arr) - 1:  # Single loop logic
    if arr[i] > arr[i + 1]:  # Compare adjacent elements
        # Swap if elements are out of order
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = 0  # Restart the loop after a swap to ensure all elements are checked
    else:
        i += 1  # Move to the next element if no swap is needed

print("Sorted array:", arr)

"""

num=[5, 3, 8, 6, 2, 7, 4, 1]

i=0
while i< len(num)-1:
    if num[i]>num[i+1]:
        num[i],num[i+1]=num[i+1],num[i]
        i=0
    else:
        i+=1
print("Sorted array:- ",num)
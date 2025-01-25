

"""num=[5,6,8,2,4,5,6,7]
for i in range(len(num)-1,0,-1):
    for j in range(i):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
print(num)
"""
"""num=[5,6,8,2,4,5,6,7]
l=len(num)

for i in range(l):
    if num[i]>num[i+1]:
        print(num[i])
        num[i],num[i+1]=num[i+1],num[i]
print(num)"""

arr = [5, 3, 8, 6, 2, 7, 4, 1]

i = 0  # Index for the loop
while i < len(arr) - 1:  # Single loop logic
    if arr[i] > arr[i + 1]:  # Compare adjacent elements
        # Swap if elements are out of order
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = 0  # Restart the loop after a swap to ensure all elements are checked
    else:
        i += 1  # Move to the next element if no swap is needed

print("Sorted array:", arr)
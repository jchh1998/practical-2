highest = 0
lowest = 1000000
arr = [567,123,76541,2123]
for i in range(len(arr)):
    if arr[i] > highest:
        highest = arr[i]
    if arr[i] < lowest:
        lowest = arr[i]

print(highest)
print(lowest)

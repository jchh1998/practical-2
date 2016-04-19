n = 5
arr = [1,2,3,4,5]
final = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == n:
            if arr[i] not in final:
                final.append(arr[i])
                final.append(arr[j])
print(final)

A = [21, 34, 41, 22, 35]
B = [61, 34, 45, 21, 11]
interArray = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            interArray.append(A[i])

print(interArray)

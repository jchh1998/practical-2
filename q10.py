A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
interArray = []

for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            if A[i] == B[j] == C[k]:
                interArray.append(A[i])

print(interArray)

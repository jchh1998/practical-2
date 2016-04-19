A = [1,2,3,1,2,3,4,5]
B = []
for i in range(len(A)):
    if A[i] not in B:
        B.append(A[i])

print(B)

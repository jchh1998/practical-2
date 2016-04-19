A = [10, 5, 3, 4, 3, 5, 6]
for i in range(len(A)):
    if A.count(A[i]) > 1:
        print(A[i])
        break

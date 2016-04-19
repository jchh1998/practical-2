A = [1,2,3,4,5,1,1,2,3,3]
duplicate = 0
for i in range(len(A)):
    if A.count(i) > 1:
        duplicate += 1

print(duplicate)

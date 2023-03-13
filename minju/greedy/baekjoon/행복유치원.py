n, k = map(int, input().split())
student = list(map(int, input().split()))

boundary = []
for i in range(1,n):
    boundary.append(student[i]-student[i-1]) 

boundary.sort(reverse=True)

print(sum(boundary[k-1:]))

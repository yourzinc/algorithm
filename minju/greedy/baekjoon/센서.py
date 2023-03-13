n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

if k>=n:
    print(0)
else:
    sensor.sort()
    boundary = []
    for i in range(1, len(sensor)):
        boundary.append(sensor[i]-sensor[i-1])
    boundary.sort(reverse=True)
    print(sum(boundary[k-1:]))

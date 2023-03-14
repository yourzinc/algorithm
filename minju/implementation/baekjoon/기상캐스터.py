h, w = map(int, input().split())
cmap = []
for i in range(h):
    cmap.append(list(input()))
    
for i in range(h):
    cloud = 0
    sub = []
    for j in range(w):
        if cloud == 0:
            if cmap[i][j] == 'c':
                sub.append(str(cloud))
                cloud = j + 1
            else:
                sub.append('-1')
                cloud = 0
        else:
            if cmap[i][j] == '.':
                sub.append(str(j-cloud+1))
            else:
                sub.append('0')
                cloud = j + 1
    print(' '.join(sub))

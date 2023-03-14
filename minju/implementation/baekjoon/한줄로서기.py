n = int(input())
arr = list(map(int, input().split()))
hight = list(range(1, n+1, 1))

rarr = arr[::-1]
rhight = hight[::-1]

for a, h in zip(rarr,rhight):
    if h - a == h:
        continue
    else:
        hight.insert(hight.index(hight[hight.index(h)+1:][:a][-1]),hight.pop(hight.index(h)))
        
for i in hight:
    print(i, end=' ')

H, W = map(int, input().split())

heights = list(map(int, input().split()))

answer = 0

block = [ [ 0 for _ in range(W)] for _ in range(H)]

for i in range(len(heights)):
    for h in range(heights[i]):
        block[h][i] = 1
    
# for b in block:
#     print(b)
    
for i in range(H):
    this_block = block[i]
    for j in range(1, W):
        if block[i][j] != 0:
            continue
        # block[i][j]
        left = list(this_block[:j])
        right = list(this_block[j+1:])
        if  left.count(1) > 0 and right.count(1) >0:
            answer +=1
            block[i][j] = 2
            
# print("Result :", answer)
# for b in block:
#     print(b)

print(answer)
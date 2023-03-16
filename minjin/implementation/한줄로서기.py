n = int(input())
records = list(map(int, input().split()))
answer = [0] * n

for idx in range(len(records)):
    taller_left = records[idx]
    for i in range(len(answer)):
        if answer[i] == 0:
            if taller_left > 0:
                taller_left -= 1
            else:
                answer[i] = idx + 1
                break
print(*answer)
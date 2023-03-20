import sys
input = sys.stdin.readline

rooms = []
p, m = map(int, input().strip().split())
for _ in range(p):
    level, nickname = input().strip().split()
    level = int(level)
    entered = False
    if rooms:
        for r in rooms:
            if abs(r[0] - level) <= 10 and len(r[1]) < m:
                r[1].append((level, nickname))
                entered = True
                break
    if not rooms or not entered:
        rooms.append([level, [(level, nickname)]])

for room in rooms:
    room[1].sort(key=lambda x:x[1])
    if len(room[1]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for level, nickname in room[1]:
        print(level, nickname)

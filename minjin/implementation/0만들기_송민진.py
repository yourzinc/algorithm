import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
for case in range(tc):
    if case > 0:
        print()

    n = int(input())
    answer = []

    numbers = deque([])
    for x in range(1, n+1):
        numbers.append(x)

    q = deque([numbers.popleft()])

    # 1. 모든 수식들 구하기
    while numbers:
        new_num = numbers.popleft()

        tmp = deque([])
        while q:
            material = q.popleft()
            tmp.append(str(material) + " " + str(new_num))
            tmp.append(str(material) + "+" + str(new_num))
            tmp.append(str(material) + "-" + str(new_num))
        q = tmp

    # 모든 수식 계산하여 0인 아이들만 남기기
    while q:
        checking = q.popleft()
        result = eval(checking.replace(" ", ""))
        if result == 0:
            answer.append(checking)

    for a in answer:
        print(a)
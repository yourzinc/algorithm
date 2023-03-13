import sys
input = sys.stdin.readline

n = int(input().strip())
balls = input().strip()     # ★★★★★ sys 붙일 떈 strip() 습관화하자. 이걸로 오답이 갈림
moves = []

r_to_left = balls.lstrip("R").count("R")
moves.append(r_to_left)

r_to_right = balls.rstrip("R").count("R")
moves.append(r_to_right)

b_to_left = balls.lstrip("B").count("B")
moves.append(b_to_left)

b_to_right = balls.rstrip("B").count("B")
moves.append(b_to_right)

print(min(moves))
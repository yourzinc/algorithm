# 3/25 토 5:52 - 6:13
# [BOJ] A와 B 2

# 두 문자열 S, T 가 주어졌을 때,
# S -> T 로 바꾸는 게임 

# 1) 문자열 뒤에 A 를 추가한다
# 2) 문자열 뒤에 B 를 추가하고 문자열을 뒤집는다

# S 를 T로 만들 수 있는지 없는지 알아내기

S = input()
T = input()

global possible
possible = False

def BT(S, T):
    if len(S) == len(T):
        if S == T:
            global possible
            possible = True
        return
    
    NS = S + 'A'
    if NS in T or NS[::-1] in T:
        BT(NS, T)
    
    NS = S + 'B'
    if NS in T or NS[::-1] in T:
        BT(NS[::-1], T)

BT(S,T)
print(int(possible))
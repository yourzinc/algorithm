import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(list(map(str,range(1,int(input())+1,1))))

op =  [' ', '+', '-']     
for i in range(len(num)):
    for j in (list(product(op, repeat=len(num[i])-1))):
        ex = ''.join(list(sum(list(zip(num[i],j)), ()))+[num[i][-1]])
        if eval(ex.replace(' ','')) == 0:
            print(ex)
    print('')

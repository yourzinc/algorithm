from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
    
people = list(range(0,n))
start = list(combinations(people,n//2))

diff = 1e9
for i in range(len(start)):
    start_stats = 0 
    for x in list(combinations(start[i],2)):
        start_stats = start_stats + arr[x[0]][x[1]] + arr[x[1]][x[0]]

    link = list(set(people)-set(start[i]))    
    link_stats = 0 
    for y in list(combinations(link,2)):
        link_stats = link_stats + arr[y[0]][y[1]] + arr[y[1]][y[0]]

    diff = min(diff,abs(start_stats - link_stats))
    
print(diff)

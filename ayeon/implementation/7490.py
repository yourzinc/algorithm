N = int(input())

def check(result):
    a = 0
    result = result.replace(" ", "")
    n = ''
    for i in range(len(result)-1, -1, -1):
        if result[i] == '+' :
            a += int(n)
            n = ''
        elif result[i] == '-':
            a -= int(n)
            n = ''
        else:
            n = result[i] + n
    
    if n != '':
        a += int(n)
        
    if a == 0:
        return True
    return False
    

def Recursive(step, arr, result, answer):
    if step == len(arr)-1:
        result = result+str(arr[step])
        if check(result):
            answer.append(result)
        return

    Recursive(step+1, arr, result+str(arr[step])+' ', answer)
    Recursive(step+1, arr, result+str(arr[step])+'+', answer)
    Recursive(step+1, arr, result+str(arr[step])+'-', answer)
 
answer = []  

for i in range(N):
    M = int(input())
    arr = [ i+1 for i in range(M) ]
    result = ""
    
    Recursive(0, arr, result, answer)
    answer.append("")

answer.pop()
for a in answer:
    print(a)

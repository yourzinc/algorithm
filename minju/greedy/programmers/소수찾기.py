from itertools import permutations #순열

def solution(numbers):
    answer = 0

    num = list(numbers)
    cnum = []

    for  i in range(1,len(num)+1):

        for c in (permutations(num, i)):
            cnum.append(int(''.join(list(c)))) #개수 별로 모든 조합

    cnum = list(set(cnum))


    def is_prime_number(x):

        if x<2:
            return False

        for i in range(2, x):

            if x % i == 0:
                return False # 소수가 아님

        return True # 소수임

    isprime = []

    for i in cnum:
        if is_prime_number(i) ==True:
            isprime.append(i)
    
    answer = len(isprime)    

    return answer

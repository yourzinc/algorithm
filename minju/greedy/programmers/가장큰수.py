def solution(numbers):
    numbers = list(map(str, numbers)) #리스트로 들어갈때 문자열로 들어감
    print(numbers)
    numbers.sort(key = lambda x : x*3, reverse = True) #바로적용
    return str(int(''.join(numbers))) 

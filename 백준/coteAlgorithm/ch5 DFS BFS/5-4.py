#재귀 함수 종료 예제
def recursive_function(i):
    if i==10:
        return
    print('재귀 함수를 호출합니다')
    recursive_function(i+1)

recursive_function(1)


# 피보나치 수열 모듈 개발
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b= b, a+b
        
        
# java에서 실행시 가장 먼저 실행되는 메소드, 없으면 실행 안 되되는 특수 메소드: main
# python 명령어로 직접 호출시에만 자동 실행되는 특수 문법
# 외부에서 모듈로 import 시에는 무시되는 영역

if __name__ == "__main__":
    print("python을 직접 명령어로 실행시 자동 호출되는 영역")
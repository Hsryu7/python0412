#function1.py
#1) 함수를 정의
def setValue(newValue):
    x = newValue
    print("지역번수:", x)

#2)호출(중단점을 지정)
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

#호출
print(swap(3,4))

#스코핑룰(LGB)
x=1
def func1(a):
    return x+a

print(func1(1))

def func2(a):
    x=5
    return x+a

print(func2(1))

#람다함수
 
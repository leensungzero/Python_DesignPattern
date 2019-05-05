"""
메타클래스란 간단하게 말하자면 클래스의 클래스이다.
즉, 클래스는 자신의 메타클래스의 인스턴스다.
메타클래스를 사용하면 이미 정의된 파이썬 클래스를 통해 새로운 형식의 클래스를 생성할 수 있다.
ex) MyClass라는 객체가 있다면 MyKls라는 메타클래스를 생성해 MyClass의 행위를 재정의할 수 있다.

자세히 알아보자면
파이썬은 모든 것이 객체다.
a=5라면 type(a)는 <type 'int'>를 반환한다. a는 int형 변수라는 뜻
하지만 type(int)는 <type 'type'>를 반환한다. int의 메타클래스는 type 클래스라는 의미

클래스는 메타클래스가 정의
class A 구문으로 클래스를 생성하면 파이썬은 A = type(name, bases, dict)를 실행
 - name: 클래스명
 - base: 베이스 클래스
 - dict: 속성값

이미 정의된 메타클래스가 있다면 파이썬은 A = MetaKls(name, bases, dict)를 실행해 클래스를 생성
"""


class MyInt(type):
    # __call__메소드는 이미 존재하는 클래스의 객체를 생성할 때 호출되는 파이썬의 특수 메소드
    def __call__(cls, *args, **kwargs):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# int(4, 5)로 int 클래스를 생성하면 MyInt 메타클래스의 __call__ 메소드가 호출
i = int(4, 5)


"""
실행결과 예시
***** Here's My int ***** (4, 5)
Now do whatever you want with these objects...
"""


# 메타클래스가 클래스와 객체 생성을 제어한다면 싱글톤을 생성하는 용도로 사용할 수 있다는 의미이다.
# (클래스 생성과 인스턴스화를 제어하기 위해 메타클래스는 __new__와 __init__ 메소드를 오버라이드한다.)

# 메타클래스를 사용해 싱글톤 패턴을 구현한다면?

class MetaSingleton(type):
    _instaces = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instaces:
            cls._instaces[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instaces[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)


"""
실행결과 예시
<__main__.Logger object at 0x000001B5363B6E48> <__main__.Logger object at 0x000001B5363B6E48>
"""
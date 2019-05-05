"""
싱글톤 디자인 패턴은 글로벌하게 접근 가능한 단 한 개의 객체만을 허용하는 패턴이다.
로깅이나 데이터베이스 관련 작업, 프린터 스풀러 등의 애플리케이션에서 동일한 리소스에 대한 동시 요청의 충돌을
막기 위해 한 개의 인스턴스만 필요한 경우에 주로 쓰인다.

싱글톤 디자인 패턴의 목적
 - 클래스에 대한 단일 객체 생성
 - 전역 객체 제공
 - 공유된 리소스에 대한 동시 접근 제어

싱글톤 디자인 패턴 구현 방법
 - 생성자를 private로 선언하고 객체를 초기화하는 static 함수를 만들면 간단하게 싱글톤을 구현가능
 - 첫 호출에 객체가 생성되고 클래스는 동일한 객체를 계속 반환

 - 하지만 파이썬에서 생성자를 private로 선언할 수 없기 때문에 다른 방법이 필요함
"""



class Singleton(object):
    # 처음에 __new__함수 호출 후 객체를 생성 할당하고, __new__함수가 __init__함수를 호출함으로써 객체에서 사용할 초기값들을 초기화한다.
    def __new__(cls, *args, **kwargs): # __init__함수 호출 전 __new__함수가 클래스 자체를 받아 객체를 생성 할당 하게 된다.
        if not hasattr(cls, 'instance'): # cls에 instance라는 멤버가 있는지 확인
            cls.instance = super(Singleton, cls).__new__(cls) # 이미 객체가 생성됐음을 확인하고 해당 인스턴스를 반환
        return cls.instance


s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)

"""
실행결과 예시
Object created <__main__.Singleton object at 0x000001E7BCE35898>
Object created <__main__.Singleton object at 0x000001E7BCE35898>
"""
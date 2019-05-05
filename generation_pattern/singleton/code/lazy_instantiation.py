"""
게으른 초기호(lazy instantiation)는 싱글톤 패턴의 한 종류

- 모듈을 임포트할 때 아직 필요하지 않은 시점에 실수로 객체를 미리 생성하는 경우가 생김
- 게으른 초기화는 인스턴스가 꼭 필요할 때 생성
- 사용할 수 있는 리소스가 제한적인 상황일 때 객체가 꼭 필요한 시점에 생성하는 방식
"""


class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton() # 클래스를 초기화했지만 객체는 생성하지 않음
print("object created", Singleton.getInstance()) # 객체 생성
s1 = Singleton() # 객체는 이미 생성됐음


"""
실행결과 예시
 __init__ method called..
 __init__ method called..
object created <__main__.Singleton object at 0x000001EE99945978>
Instance already created: <__main__.Singleton object at 0x000001EE99945978>
"""
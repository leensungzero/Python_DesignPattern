"""
GoF의 싱글톤 디자인 패턴에 의하면 반드시 한 개의 클래스 객체만 존재해야 한다.
알렉스 마르텔리는 상태를 공유하는 인스턴스가 필요하다고 주장
객체 생성 여부보다는 객체의 상태와 행위가 더 중요하다고 이야기

모노스테이트 싱글톤 패턴(monostate singleton patter)은 이름 그대로 모든 객체가 같은 상태를 공유하는 패턴
"""


class Borg:
    __shared_state = {"1": "2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b': ", b) # b와 b1은 다른 객체
print("Borg Object 'b1: ", b1)
print("Object State 'b':", b.__dict__) # b와 b1은 상태를 공유
print("Object State 'b1':", b1.__dict__)


"""
실행결과 예시
Borg Object 'b':  <__main__.Borg object at 0x000001DEFAF160F0>
Borg Object 'b1:  <__main__.Borg object at 0x000001DEFAF16208>
Object State 'b': {'1': '2', 'x': 4}
Object State 'b1': {'1': '2', 'x': 4}
"""
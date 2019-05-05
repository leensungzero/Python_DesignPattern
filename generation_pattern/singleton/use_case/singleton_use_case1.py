"""
데이터베이스 기반 애플리케이션에서 싱글톤 패턴을 적용한 사례

여러 서비스가 한 개의 DB를 공유하는 구조.
안정된 클라우드 서비스를 설계하려면 다음 사항들을 반드시 명심해야 한다.
 - 데이터베이스의 일관성을 보존해야 한다. 연산 간의 충돌이 없어야 한다.
 - 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야 한다.
"""
import sqlite3


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)


"""
실행결과 예시
Database Objects DB1 <sqlite3.Cursor object at 0x00000228DB1F7DC0>
Database Objects DB2 <sqlite3.Cursor object at 0x00000228DB1F7DC0>
"""


# 코드 살펴보기

"""
1. MetaSingleton이라는 메타클래스를 생성한다. __call__ 파이썬 메소드를 사용해 싱글톤을 생성한다.
2. Database 클래스는 MetaSingleton 메타클래스의 도움으로 싱글톤 역할을 한다. 단 한 개의 database 클래스 객체만 생성한다.
3. 웹 앱이 DB 연산을 요청할 때마다 database 클래스를 생성하지만 내부적으로는 한 개의 객체만 생성된다.
   따라서 데이터베이스의 동기화가 보장된다. 리소스를 적게 사용해 메모리와 CPU 사용량을 최적화할 수 있다.
   
**이제 단일 웹 앱 형태가 아닌 여러 웹 앱이 같은 DB에 접속하는 상황을 생각해보자**
이 경우 각 웹 앱이 DB에 접근하는 싱글톤을 생성하기 때문에 싱글톤 패턴에 적합하지 않다.
DB 동기화가 어렵고 리소스 사용량이 많은 경우다.
싱글톤 패턴보다 연결 풀링 기법을 사용하는 것이 더 효율적이다.
"""
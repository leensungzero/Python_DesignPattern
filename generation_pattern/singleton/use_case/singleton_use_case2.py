"""
인프라 상태를 확인하는 서비스(예를 들면 Nagios)를 구현해보자

우선 HealthCheck 클래스를 싱글톤으로 구현한다.
상태를 확인해야 하는 서버의 목록을 만들고 목록에서 제거된 서버의 상태는 확인하지 않아야 한다.

코드를 살펴보면
hc1과 hc2는 동일한 객체다.

addServer() 메소드는 서버를 몰고에 추가한다.
서비스는 목록의 각 서버의 상태를 확인한다.
changeServer() 메소드는 서버를 목록에서 제거하고 새로운 서버를 추가한다.
따라서 서비스는 두 번째 실행될 때는 바뀐 서버 목록을 참조한다.
"""


class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for servers (1)..")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer()
print("Schedule health check for servers (2)..")
for i in range(4):
    print("Checking ", hc2._servers[i])


"""
실행결과 예시
Schedule health check for servers (1)..
Checking  Server 1
Checking  Server 2
Checking  Server 3
Checking  Server 4
Schedule health check for servers (2)..
Checking  Server 1
Checking  Server 2
Checking  Server 3
Checking  Server 5
"""
# 부모 클래스에서 추상 메소드로 선언한 메소드에 대해서는 반드시 상속 받은 자식 클래스에서 해당 기능을 구현해야 함

from abc import *

class NetworkAdapter(metaclass=ABCMeta) :
    @abstractmethod
    def connect(self) :
        pass

class FiveG(NetworkAdapter) :       # NetworkAdapter로부터 상속 받음
    def __init__(self, company) :
        self.company = company
    def connect(self) :
        print(f"{self.company} 5G로 연결하였습니다")

class WiFi(NetworkAdapter) :       # NetworkAdapter로부터 상속 받음
    def __init__(self, company) :
        self.company = company
    def connect(self) :
        print(f"{self.company} Wi-Fi로 연결하였습니다")

class LTE(NetworkAdapter) :       # NetworkAdapter로부터 상속 받음
    def __init__(self, company) :
        self.company = company
    def connect(self) :
        print(f"{self.company} LTE로 연결하였습니다")

net = input("연결할 네트워크를 선택하세요 [1]5G [2]WiFi [3]LTE : ")
if net == "1" :
    adapter = FiveG("KT Mega PASS")
    adapter.connect()
elif net == "2" :
    adapter = WiFi("SK Telecom")
    adapter.connect()
elif net == "3" :
    adapter = LTE("LG Telecom")
    adapter.connect()
else : print("연결할 네트워크가 없습니다")

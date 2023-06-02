# TV 클래스와 생성자
# 생성자 키워드 : __init__
# 생성자에는 self라는 키워드를 사용해 내부의 값을 초기화

class TV :
    def __init__(self, name, is_on, channel, volume) :
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on) :
        self.is_on = is_on
    def set_channel(self, cnl) :
        self.channel = cnl
    def set_volume(self, vol) :
        self.volume = vol
    def get_on(self) :
        return self.is_on
    def get_channel(self) :
        return self.channel
    def get_volume(self) :
        return self.volume
    def view_tv(self) :
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = TV("LG", False, 11, 10)
samsung_tv = TV("SAMSUNG", False, 20, 20)

lg_tv.view_tv()
samsung_tv.view_tv()

lg_tv.set_on(True)
lg_tv.set_volume(29)
lg_tv.set_channel(1)
lg_tv.view_tv()
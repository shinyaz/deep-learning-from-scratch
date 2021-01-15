# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name) -> None:
        self.name = name
        print("Initialized!")
    
    def hello(self) -> None:
        print("Hello " + self.name + "!")
    
    def goodbye(self) -> None:
        print("Good-bye " + self.name + "!")

m = Man("David")
m.hello()
m.goodbye()
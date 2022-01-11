class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print("안녕하십니까? 저는 {0}살 {1}에 사는 {2}입니다.".format(self.age, self.address, self.name))
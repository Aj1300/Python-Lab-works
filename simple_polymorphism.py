class movie1:
    def __init__(self,name):
        self.name=name
    def details(self):#@#@#@#@#@@@#@@#@#@@@@@@@@@@@@@@@@@@@@
        print("movie name: ",self.name)
class movie2:
    def __init__(self,name,actor):
        self.name=name
        self.actor=actor
    def details(self):#@###################
        print("movie name: ",self.name," ,actor:  ",self.actor)

x=movie1("iron man")
y=movie2("thor","chris hem")

x.details()
y.details()
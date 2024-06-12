class marvel:
    def __init__(self,name):
        self.hname=name
    def displayname(self):
        print(self.hname)
class xmen(marvel):
    def __init__(self, hname):
        marvel.__init__(self,hname)
obj=xmen("deadpool")
obj.displayname()
# next same program with super
class marvel:
    def __init__(self,name):
        self.hname=name
    def displayname(self):
        print(self.hname)
class xmen(marvel):
    def __init__(self, hname):
        super().__init__(hname)
obj=xmen("deadpool")
obj.displayname()
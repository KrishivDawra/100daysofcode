#Here below i am using constructor by using __init__
class person:
    def __init__(self,n, o):
        print("Helloo")
        self.name=n
        self.occ=o
    def info(self):
        print(self.name," is a ",self.occ)

a=person("Krishiv","Developer")
b=person("Namit","MERN stack developer")
c=person("tulika","HR")
a.info()
b.info()
c.info()

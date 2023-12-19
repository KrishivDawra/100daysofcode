#Basic intro of oops class and objects
class person:
    name="krishiv"
    status="student"
    age=17
    def info(self):
        print(self.name," is a ",self.status)

a=person()
b=person()
c=person()

a.name="Krish"
a.status="developer"
a.info()

b.name="Dawra"
b.status="MERN"
b.info()
c.info()

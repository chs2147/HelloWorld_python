class Human:  # Human Class
    age = 0
    name = ''

    def __init__(self):
        self.name = 'John Doe'

    def __del__(self):
        print 'Human Out'

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def printHuman(self):
        print self.name
        print self.age
        print '\n'


class Man(Human):  # Man Class / Sub
    sex = 'Male'
    interests = 'Electoronics'

    def __init__(self):
        self.name = 'John Doe'

    def __del__(self):
        print 'Man out'

    def printHuman(self):
        print self.name
        print self.age
        print self.sex
        print self.interests
        print '\n'


class Woman(Human):  # Woman Class / Sub
    sex = 'Female'
    interests = 'Fashions'

    def __init__(self):
        self.name = 'Jane Doe'

    def __del__(self):
        print 'Woman out'

    def printHuman(self):
        print self.name
        print self.age
        print self.sex
        print self.interests
        print '\n'


A = Human()
A.printHuman()
A.setName('Alpha')
A.setAge(10)
A.printHuman()
A.name = 'Alpha2'
A.age = 100
A.printHuman()

B = Man()
B.printHuman()
B.setName('Bravo')
B.setAge(15)
B.printHuman()

C = Woman()
C.printHuman()
C.setName('Charlie')
C.setAge(20)
C.printHuman()
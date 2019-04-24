class Person:

    # Init method
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name

class PersonDetail:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        print 'Hello, my name is',self.name
        print 'And I am {0} year(s) old.'.format(self.age)


p = Person('Leslie')
m = PersonDetail('Hell Boy', 20)


p.say_hi()
m.say_hi()
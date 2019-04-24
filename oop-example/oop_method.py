class Person:

    message = ''

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return ('My name is {0}').format(self.message)

    def say_hi(self):
        print('Hello, how are you?')

p = Person('Leslie')
p.say_hi()

print p
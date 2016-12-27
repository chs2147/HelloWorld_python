# Basic print command
print "Hello World !!"

# Multi-line print command
print """This is multiline test.
Good bye 2016, Welcom 2017!
"""

#String formatting
age = 20
name = 'Jenny'

print "{0} was {1} years old when she wrote this book.".format(name,age)
print "My name is {0}".format(name)

#Floating point expression
print "{0:.4f}".format(2.0/3)

#Text with fill blank with fixed character
print "{0:-^11}".format("HELLO")

#Keyword alternation
print "{name} wrote {book}".format(name='Jenny',book='Harry Potter')

#Continue to print on same line
print "one ",
print "two ",
print "three"
print "END"

#Escape character
print "What\'s your name?"
print "I am NIRO.\nThe smart SUV."
print "100\t200\t300"
print "- First Item \
- Second Item \
- Third Item"

#Show raw text
print r"Newlines are indicated by \n"



ab = { 'Leslie' : 'chs2147@naver.com',
       'Larry' : 'larry@wall.org',
       'Matsumoto' : 'matz@ruby-lang.com',
       'Spammer' : 'spammer@hotmail.com'
       }

print "Leslie's address is", ab['Leslie']

# Deleting a key-value pair
del ab['Spammer']

print '\nThere are {0} contacts in the address-book.\n'.format(len(ab))

for name, value in ab.items():
    print 'Contact {0} at {1}'.format(name, value)

#Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\nGuide's address is", ab['Guido']


bri = set(['brazil','russia','india'])

print 'India in bri?', 'india' in bri
print 'USA in bri?', 'USA' in bri

bric = bri.copy()
bric.add('china')
print 'BRIC is supset of BRI?', bric.issuperset(bri)

bri.remove('russia')
print 'BRI intersect BRIC =', bri.intersection(bric)

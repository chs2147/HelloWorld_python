def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''

    total = 0
    for i in args:
        total += pow(i, power)

    return total

print powersum(2,3,4,5,6,7)
print powersum(1,2,3)
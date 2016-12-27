number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # New block starts here
    print 'Congratulations, you guessed it.'
    # New block ends here
elif guess < number:
    # Another block
    print 'No, it is a little higher than that'

else:
    print 'No, it is a little lower than that'

# This last statement is always executed, after the if statement is executed.
print 'Done'

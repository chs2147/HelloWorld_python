def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def convertToFullText(text):
    forbidden = ('.','?','!',':',';','-','(',')','[',']',',','/',' ')

    for symbol in forbidden:
        text = str.replace(text, symbol,'')

    return str.lower(text)

# Original text
something = 'Rise to vote, sir.'
print "Original Text:", something

print

# Convert text to full text
something = convertToFullText(something)
print "Full Text:", something

if is_palindrome(something):
    print "Yes, it is a palindrome."
else:
    print "No, it is not a palindrome."

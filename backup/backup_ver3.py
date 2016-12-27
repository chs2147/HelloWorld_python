import os
import time

# Files and directories to be backed up are specified in a list
source = ['/Users/chs2147/Documents/FineDrive','/Users/chs2147/Documents/protoNow']

# Target directory for backup
target_dir = '/Users/chs2147/Documents/temp'

# Target file name
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from console input
comment = raw_input('Enter a comment --> ')

# Check comment
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    # Replace space character to under stroke from input text
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

# Create target directory
if not os.path.exists(today):
    # Make directory
    os.mkdir(today)
    print "Successful created directory", today

# Zip command
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run backup
print "Zip command =", zip_command
print "Running:"

if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAiLED"
import os
import time

# Files and directories to be backed up are specified in a list
source = ['/Users/chs2147/Documents/Snagit','/Users/chs2147/Documents/protoNow']

# Target directory for backup
target_dir = '/Users/chs2147/Documents/temp'

# Target file name
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory
if not os.path.exists(target_dir):
    # Make directory
    os.mkdir(target_dir)

# Zip command
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run backup
print "Zip command =", zip_command
print "Running:"

if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAiLED"
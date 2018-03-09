import sys 
import os
from subprocess import call 

if len(sys.argv)>1:
    if sys.argv[1]=='y':
        os.system('ls -lah')
    else:
        call('top')
else:
    print("No arguments.")
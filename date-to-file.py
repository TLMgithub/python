#!/usr/local/anaconda/bin/python

from datetime import datetime
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("date and time:",date_time)

import sys
original_stdout = sys.stdout # Save a reference to the original standard output
with open('/mnt/date.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print("date and time:",date_time)
    sys.stdout = original_stdout # Reset the standard output to its original value

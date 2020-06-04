#!/usr/bin/python

from datetime import date
today = date.today()
#print("Today's date:", today)

import sys
original_stdout = sys.stdout # Save a reference to the original standard output
with open('date.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print("Today's date:", today)
    sys.stdout = original_stdout # Reset the standard output to its original value

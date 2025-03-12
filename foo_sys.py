import time 
import sys


txt = "Hello old snake!"

for i in range(len(txt)):
    sys.stdout.write(f'\r{txt[:i]}')
    
    time.sleep(0.5)
    sys.stdout.flush()
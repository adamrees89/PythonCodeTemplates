## Credit to Haider Imtiaz

#Check free RAM

import psutil
 
def bytes_format(n):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if n < 1024.0:
            return "%3.1f %s" % (n, x)
        n /= 1024.0
response=list(psutil.virtual_memory())
# Total ram.
print("Total Ram:", bytes_format(int(response[0])))
# Ram used.
print("Ram used :", bytes_format(int(response[3])))
 
# Ram free.
print("Ram Free :", bytes_format(int(response[1])))
 
# Output:
#Total Ram: 15.8 GB
#Ram used : 9.2 GB
#Ram Free : 6.7 GB

#---------------------------------------------------

## Credit to Haider Imtiaz

# ShutDown Window
import os
os.system('shutdown -s -t 0')

#---------------------------------------------------
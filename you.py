import sys
import os

f = open('cmd.txt', 'w')   
a = len(sys.argv)-1
for i in range(a):
    i += 1
    print "NO %d argv = %s" % (i,sys.argv[i])
    f.write(sys.argv[i]+'\n')
f.close()

#os.startfile('config.py')
f = os.popen ("/usr/bin/python config.py",'r')
print f.read()

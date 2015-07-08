import sys
import math

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage:", sys.argv[0], "infile  outfile"
    sys.exit(1)

ifile = open(infilename , ’r’)
ofile = open(outfilename , ’w’)

def  myfunc(y):
    if y  >= 0.0:
        return y**5*math.exp(-y)
    else:
        return  0.0

for  line in ifile:
    pair = line.split()
    x = float(pair[0])
    y = float(pair[1])
    fy = myfunc(y)
    ofile.write(’%g %12.5e\n’ % (x,fy))

ifile.close()
ofile.close()

import sys

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print "Usage:", sys.argv[0], "infile outfile"
    sys.exit(1)

ifile = open(infilename, 'r')
ofile = open(outfilename, 'w')

for line in ifile:
    arr = line.split()
    avg = sum(map(lambda x: float(x), arr)) / len(arr)
    ofile.write('%s %12.6e\n' % (line[:-1] if line[-1] == '\n' else line, avg))

ifile.close()
ofile.close()

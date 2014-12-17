def makelist():
    f = open("data.txt", "r")
    lines = f.read().split('\n')
    for i in xrange(len(lines)):
        lines[i] = lines[i].split()
    print lines
    f.close()
makelist()

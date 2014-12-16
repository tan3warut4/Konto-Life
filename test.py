f = open("data.txt", "r")
lines = f.read().split('\n')
sent ="asd"
for i in xrange(len(lines)):
    lines[i] = lines[i].split()
for j in lines:
    if j[0] == sent:
        print 2
f.close()

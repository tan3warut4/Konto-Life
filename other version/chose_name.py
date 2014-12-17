def chose_name(vari):
    f = open("data.txt", "r")
    lines = f.read().split('\n')
    for i in xrange(len(lines)):
        lines[i] = lines[i].split()
    for i in xrange(len(lines)):
        tan = lines[i]
        for j in xrange(len(tan)):
            if tan[j] == vari:
                return tan[j+1]
print chose_name(raw_input())

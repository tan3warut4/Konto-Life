f = open("data.txt", "r")
lines = f.readlines()
f.close()
f = open("data.txt", "w")
for line in lines:
    if line != 'tan 4000 400.0'+'\n':
        f.write(line)
f.close()

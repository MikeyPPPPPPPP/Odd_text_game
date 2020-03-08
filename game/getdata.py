a = open('game_data', 'r')
getthem = a.read()
s = getthem.split(',')
print(s)
fi = []
temp = {}
for x in s:
    #print(x)
    e = x.split(':')

    print(str(e))
    fi.append(e)

print(fi)
for x in (fi):
    print(x[0],'=',x[1])
    temp[x[0]]=x[1]

print(temp)
print(temp['name'])
a.close()

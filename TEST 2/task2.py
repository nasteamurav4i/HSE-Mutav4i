import re

with open('mystem.xml', 'r', encoding='utf-8') as f:
    text = f.readlines()
d ={}
for line in text:

    gr = re.findall(r'gr=\"(.+)?\"', line)
    for i in gr:
        if i in d.keys():
            d[i] +=1
        else:
            d[i] = 1
sort_d = sorted(d.items(), key=lambda x: x[1], reverse = True)
with open('result2.txt', 'w') as f:
    for i in sort_d:
        line = i[0]+str(i[1])+'\n'
        f.write(line)


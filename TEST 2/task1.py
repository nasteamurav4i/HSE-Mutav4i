import re

with open('mystem.xml', 'r', encoding='utf-8') as f:
    text = f.read()

t = re.findall(r'\n', text)
t2 = re.sub(r'\n', '  ',text)
t3 = re.search(r'<body>(.+)</body>', t2)
with open('result.txt', 'w') as f:
    f.write(str(len(t3.groups()[0])))


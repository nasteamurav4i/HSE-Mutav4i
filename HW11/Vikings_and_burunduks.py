import re

with open('Викинги - Википедия.html', 'r', encoding = 'utf-8') as f:
    text = f.readlines()
    
pattern1 = r'в(и́|и)кинг'
repl1 = r'бурундук'
pattern2 = r'В(и́|и)кинг'
repl2 = r'Бурундук'

burunduk_text = ''
for line in text:
    line = re.sub(pattern1, repl1, line)
    line = re.sub(pattern2, repl2, line)
    burunduk_text += line
    
with open('Burunduks.txt', 'w', encoding = 'utf-8') as f:
        f.write(burunduk_text)

import os
import re

cur_dir = os.getcwd()
pattern = r'[0-9]'
name_list = []
n = 0
tree = os.walk(cur_dir)
for path, dirs, files in tree:

    for f in files:    
        name, ext = os.path.splitext(f)
        is_num = re.search(pattern, name)
        if is_num:
            pass
        else:
            n += 1
            name_list.append(name)

print('Количество файлов, не содержащих цифр в названии:', n)

print('Названия всех файлов:')
for i in set(name_list):
    print(i)


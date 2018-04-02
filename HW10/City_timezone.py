
import re
with open('Владивосток - Википедия.html', 'r', encoding= 'utf-8') as f:
    text = f.read()
p_with_udc = r'.*(<p>.+?title=\"UTC.+?</p>)'# шаблон для поиска нужного параграфа

text = text.replace('\n', ' ')

s = re.search(p_with_udc, text)
split_pattern = r'<.+?>'
utc = re.split(split_pattern, s.groups()[0])
timezone = ''.join(utc)

with open('timezone.txt','w') as f:
    f.write('Часовой пояс:{}'.format(timezone))


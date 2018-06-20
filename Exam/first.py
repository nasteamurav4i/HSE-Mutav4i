import re
import os

def clean ():
    for file in os.listdir ():
        with open (file, 'r') as f:
            text = f.readlines ()
        for line in text:
            r = re.search('<title>(.+?)<', line)
            if r:
                title = r.group(1)
                text = re.sub ('`' , '', line)
                re.sub ('<.+?>', '', line)
        with open (file + '1', 'w', encoding='cp1251') as t:
            t.write(text)
clean ()


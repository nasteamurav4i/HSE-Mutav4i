import os

start_path = '.'

abc = set('qwertyuiopasdfghjklzxcvbnm')
nums = set('1234567890')
n = 0
for root, folders,_ in os.walk(start_path):
    for f in folders:
        if (len(set(f.lower())&abc) == 0)and(len(set(f.lower())&nums) == 0):
            n += 1

print('Количество папок с полностью кириллическими названиями: ',n)
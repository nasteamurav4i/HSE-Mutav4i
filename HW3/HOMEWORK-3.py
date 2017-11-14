print('Введите слово:')
a=input()
if len(a)==0:
    print('ERROR')
else:
    print 
    for i in range(1,len(a)+1):
        print(a[0:i])

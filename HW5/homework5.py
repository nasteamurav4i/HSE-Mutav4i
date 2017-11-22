print('Введите слова:')
words=[]
a=input()
if a=='':
    print('ERROR')
else:
    while a!='':
        if len(a)>5:
            words.append(a)
        a=input()
        if len(a)==0:
            break
if words==[]:
    print('Данное слово не подходит под условие')
else:
    for word in words:
        print(word)

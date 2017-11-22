with open('poemhw.txt', encoding='utf-8') as f:
    k=f.read()
    lines=k.splitlines()
    minimum=len(lines[0])
    maximum=len(lines[0])
    for line in lines:
        if len(line)<minimum:
            minimum=len(line)
        if len(line)>maximum:
            maximum=len(line)
    if minimum==0:
        print('ERROR(Пустая строка)')
    else:
        a=maximum/minimum
        if a==1:
            print('Длина строк одинакова')
        elif a//1==a and ((a>=2 and a<=4) or (a%100>20 and a%100%10>=2 and a%100%10<=4)):
            print('Самая короткая строка текста короче самой длинной строки в',a,'раза.')
        else:
            print('Самая короткая строка текста короче самой длинной строки в',a,'раза.')

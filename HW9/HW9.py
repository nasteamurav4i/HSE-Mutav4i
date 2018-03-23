import re

FILE_NAME = 'test.txt'
with open(FILE_NAME, 'r', encoding = 'utf-8') as f:
    text = f.read() 
pattern = re.compile(r'(\bнайд\w+)|(\bнашёл\w*)|(\bнашл[аои]\w*)|(\bнашед\w+)|(\bнайти)|(\bнаход[яи]\w+)')

all_find = pattern.findall(text.lower())
forms_set = [] 

for groups in all_find: 
    forms_set += list(groups)

for form in set(forms_set): # чтобы убрать повторения преобразуем список forms_set к типу set(множество),
                        # в нем все-таки останется одно пустое значение
    if form !='': # поэтому учтем это при выводе, введя проверку
        print(form)


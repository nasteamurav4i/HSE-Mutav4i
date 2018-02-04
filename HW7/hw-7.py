
def Words(text): #Функция разделения на слова
    words = text.split(" ")
    return words

if __name__ == "__main__":# начало программы
    all_array = [[],[]] #Создаем массив состоящий из двух массивов, 1-слова, 2-количесвто вхождений слова
    text = ""
    with open("textt.txt", encoding='utf-8') as file:
        text = file.read()
        file.close()

    text = Words(text)
    for word in text: #убираем лишние слова пробелы и пустые символы
        if word == ' ' or word == '':
            text.remove(word)

    for word in text:
        if 'ness' in word:#находим в слове ness
            try:
                index = all_array[0].index(word) #если такое слово уже есть в массиве то добавляем 1 к его количеству
                all_array[1][index] += 1
            except ValueError:
                all_array[0].append(word)#если слова в массиве ещё нет добавляем слово в массив
                all_array[1].append(1)

    i = 0

    if len(all_array[0]) != 0:
        for word in all_array[0]: #выводим результат
            i += 1
            print ("№" + str(i) + "| " + word + "  | количество вхождений - " + str(all_array[1][i-1]))
        max = 0
        for num in all_array[1]:
            if num > max:
                max = num;
        print("Максимальная частотность - " + str(max) + "\nСлова, с максимальной частотностью :")
        i = 0
        for word in all_array[0]:
            if all_array[1][i] == max:
                print(word)
            i += 1

    else:
        print("Слов с ness не найдено.")

# 2.Дан список повторяющихся элементов. Вернуть список с дублирующимися 
# элементами. В результирующем списке не должно быть дубликатов.
# myList = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# List2 = []
# for i in myList:
    # if myList.count(i) == 2:
        # List2.append(i)
# print(List2)

# 3.В большой текстовой строке подсчитать количество встречаемых слов и вернуть
# 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу 
# возьмите любую статью из википедии или из документации к языку.

sentence ='Читающая Магдалина», или «Читающая Мария Магдалина» (англ. The Magdalen Reading), — наиболее известный из трёх сохранившихся фрагментов утраченной алтарной композиции Рогира ван дер Вейдена. Созданная около 1437 года для одной из брюссельских церквей, она представляла собой изображение Девы Марии с Младенцем и святыми. Мария Магдалина, отождествляемая в западной традиции одновременно с Марией из Вифании и с безымянной грешницей, совершившей помазание Христа, изображена отрешённой от мира и погружённой в чтение священной книги. О её прежней жизни напоминают богатые одежды, в частности, украшенная драгоценными камнями юбка из золотой парчи; с их роскошью контрастирует скромный головной убор, чья своеобразная форма должна, по-видимому, напоминать о восточном происхождении святой. Рядом с сидящей Магдалиной находится её традиционный атрибут — алебастровый сосуд с миром.'
sentence = "".join([i for i in sentence.lower() if i.isalpha() or i == " "])
sentence = sentence.split()

n = 10
dictSent = dict()
for i in sentence:
    dictSent[i] = dictSent.get(i, 0) + 1
sortWord = sorted(dictSent.items(), key=lambda x: (-x[1], x[0]))[:n]
for word, count in sortWord:
    print(f"Слово '{word}' встречается {count} раз(a)")

# 4.Создайте словарь со списком вещей для похода в качестве ключа и их массой 
# в качестве значения. Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

#Dict = {'Палатка': 5, 'еда': 3, 'вода': 2, 'лопата': 1, 'ведро': 1, 'котелок': 2, 'спальник': 1}
#listKeys = list(Dict.keys())
#listItems = list(Dict.values())
#print(type(listItems))
#maxWeigth = 10
#List = []
#def func(List, index, weight):
#    print('Уже лежит: ', List)
#    for i in range(index, len(listKeys)):
#        print('Попробуем уложить ', listKeys[i])
#        if listItems[i]+ weight <= maxWeigth:
#            emptyList = List.copy()
#            emptyList.append(listKeys[i])
#            print('Положили')
#            func(emptyList, i+1, weight +listItems[i])
#        else:
#            print('Не влазит')
#    if len(List) >= 3:
#        print(List, weight)

# func(List, 0, 0)

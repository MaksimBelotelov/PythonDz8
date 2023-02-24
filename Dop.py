# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна 
# только одной данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, 
# которые будут заполнять бассейн. Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt

with open('pipes.txt', 'r', encoding='UTF-8') as f:
    list_of_perfomance =[]
    work_pipes=[]
    for line in f:
        if(line!='\n'):
            list_of_perfomance.append(int(line))
        else:
            work_pipes = f.readline().split()
            work_pipes = list(map(int, work_pipes))

    if work_pipes != []:
        if len(list_of_perfomance) != len(work_pipes):
            print('Включено больше труб, чем их есть')
        else:
            perfomance=0
            for i in work_pipes:
                perfomance += 1/list_of_perfomance[i-1]
            time = (1/perfomance) * 60
            with open('time.txt', 'w', encoding='UTF-8') as out_file:
                out_file.write(f'Бассейн заполнится за {time} минут.')
    else:
        print('Бассейн не наполнится. Все трубы выключены')





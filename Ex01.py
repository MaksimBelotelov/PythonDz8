# Напишите функцию read_last(lines, file), которая будет открывать
# определенный файл file и выводить на печать построчно последние строки
# в количестве lines (на всякий случай проверим, что задано положительное
# целое число).

def read_last(lines, file):
    if lines > 0:
        with open(file, 'r', encoding='UTF-8') as f:
            text = []
            for line in f:
                text.append(line.rstrip('\n'))
            text = text[-lines:]
            for line in text:
                print(line)
    else:
        print('Количество строк должно быть положительным числом.')

read_last(3, 'article.txt')

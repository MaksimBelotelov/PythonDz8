# Документ «article.txt» содержит текст.
# Требуется реализовать функцию longest_words(file), которая выводит 
# слово, имеющее максимальную длину (или список слов, если таковых 
# несколько).

def longest_words(file):
    with open(file, 'r', encoding='UTF-8') as f:
        max_word_len=0
        longest_words_list=[]
        for line in f:
            processing_line = line.split()
            for word in processing_line:
                if(len(word)>max_word_len):
                    max_word_len = len(word)
                    longest_words_list.clear()
                    longest_words_list.append(word)
                elif(len(word) == max_word_len):
                    longest_words_list.append(word)
    for word in longest_words_list:
        print(word)

longest_words('article.txt')
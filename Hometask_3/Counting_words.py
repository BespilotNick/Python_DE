# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


with open('test_file_for_HT_3', mode='r', encoding='utf-8') as file:
    my_string = file.readline()
    words_list = my_string.split()

word_frequency = {}

for word in words_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

sorted_list = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_list[:10]:
    print(f'Слово {key} встречается в тексте {value} раз.')
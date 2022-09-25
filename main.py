import json
import xml.etree.ElementTree as ET
from pprint import pprint

def read_files(name):
    original_text = '' 
    with open(name, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        for items in data['rss']['channel']['items']:
            original_text += ' ' + items['description']
    return original_text

def count_word(original_text: str)->dict:
    count = 0
    replaceable_characters = ':;.,'
    for replaceable in replaceable_characters:
        original_text = original_text.replace(replaceable, ' ')
    to_list = original_text.split(' ')
    word_value ={}
    for word in to_list:
        if len(word) > 6:
            word_value[word] = word_value.get(word, 0) + 1
        # else:
        #     word_value[word]=1
    return word_value

def sorting(word_value: dict)->dict:
    sorted_dict = dict(sorted(word_value.items(), key = lambda word_value:word_value[1], reverse = True))
    print('Отсортированный список', sorted_dict, '\n')
    counter = 1
    top = {}
    for word in sorted_dict:
        top[counter] = word
        counter += 1
        if counter > 2:
            break
    print('Результат сортировки: ', top, '\n')
    return top
    # return sorted_list

print()
# while True:
    # name = input("Enter file name: newsafr.json or newsafr.xml or enter exit: ")
name = "newsafr.json"
    # if name == "newsafr.json":
# top_10 = sorting(count_word(read_files(name)))
# print(top_10)
    # elif name == "exit":
    #     break
    # else:
    # print('Incorrect input, try again')

original_text = 'революция матрица матрица матрица стол 1234567, 1234567, 1234567, 12345 пандус пайтон'
expected = {'революция':1, 'матрица':3, '1234567':3}
actual = count_word(original_text)
print(actual)
assert actual == expected

print('\n')

word_value = expected
returned = {1:'матрица', 2:'1234567'}
print('Необходимо получить: ', returned, '\n')
actual1 = sorting(word_value)
print("Полученное: ", actual1)
assert actual1 == returned

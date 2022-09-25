import json
import xml.etree.ElementTree as ET
from pprint import pprint

def read_files(name):
    with open(name, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        original_text = '' 
        for items in data['rss']['channel']['items']:
            original_text += ' ' + items['description']
        return original_text

def count_word(original_text):
    a = 0
    to_list = original_text.split(' ')
    word_value ={}
    for word in to_list:
        if len(word) > 6:
            a += 1
            word_value[word]=a
        else:
            word_value[word]=1
    return word_value

def sorting(word_value):
    sorted_list = dict(sorted(word_value.items(), key = lambda word_value:word_value[1], reverse = True))
    counter = 1
    top = {}
    for word in sorted_list:
        top[counter] = word
        counter += 1
        if counter == 10:
            break
    return top
    # return sorted_list





print()
# while True:
    # name = input("Enter file name: newsafr.json or newsafr.xml or enter exit: ")
name = "newsafr.json"
    # if name == "newsafr.json":
top_10 = sorting(count_word(read_files(name)))
print(top_10)
    # elif name == "exit":
    #     break
    # else:
    #     print('Incorrect input, try again')
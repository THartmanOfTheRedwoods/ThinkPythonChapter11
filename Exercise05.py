#!/usr/bin/env python3
import json
from os.path import exists


def get_key(word):
    return ''.join(sorted(word.strip()))


def save_sorted_dict(word_dict, file_path):
    with open(file_path, 'w') as wd_file:
        json.dump(word_dict, wd_file, indent=True)


def load_sorted_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            key = get_key( word )
            key_list = word_dict.get( key, [] )
            key_list.append( word.strip() )
            word_dict[key] = key_list
    return word_dict

def load_word_dict(file_path, words_path='files/words.txt'):
    word_dict = {}
    if not exists(file_path):
        word_dict = load_sorted_dict(words_path)
        save_sorted_dict(word_dict, file_path)
    else:
        with open(file_path, 'r') as wd_file:
            word_dict = json.load(wd_file)
    return word_dict


def find_anagrams(word_list, word_dict):
    for word in word_list:
        key = get_key(word)
        if len(word_dict[key]) > 1:
            print(f'{word_dict[key]}')

if __name__ == '__main__':
    word_dict_path = 'files/word_dict.json'
    find_anagrams(['deltas', 'retainers', 'generating', 'termless'], load_word_dict(word_dict_path))
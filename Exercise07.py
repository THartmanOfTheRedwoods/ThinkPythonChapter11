#!/usr/bin/env python3

from Exercise06 import word_distance
from Exercise05 import load_word_dict

if __name__ == '__main__':
    word_dict_path = 'files/word_dict.json'
    word_dict = load_word_dict(word_dict_path)
    for k, v in word_dict.items():
        if len(v) > 1:  # These are all the words that have anagrams
            for i in range( len( v ) ): # Start with the first word
                for j in range( i + 1, len( v ) ): # Compare it to each word but not to itself
                    if word_distance( v[i], v[j] ) == 2:
                        print( f'Metathesis: {v[i]} and {v[j]}' )

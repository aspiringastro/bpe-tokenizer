# Learn Byte Pair encoding algorithm and implement a tokenizer

from collections import Counter
DEFAULT_START_TOK = '<S>'
DEFAULT_END_TOK   = '<E>'

class Encoder:
    def __init__(self, START_TOK=DEFAULT_START_TOK, END_TOK=DEFAULT_END_TOK)
        self.start_tok = START_TOK
        self.end_tok = END_TOK
    
    def build_byte_pair(self, words):
        bp_count = Counter()
        for token in words.split(' '):
            bp_count[token] += 




# 
# wget https://github.com/dwyl/english-words/blob/master/words.txt
with open('words.txt', 'r', encoding='utf-8') as f:
    text = f.read()




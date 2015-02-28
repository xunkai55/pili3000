__author__ = "badpoet"

from .vchap import VChap
import types
import string

class VBook(object):

    def __init__(self):
        self.chaps = []
        self.title = "GRE 3000"
        self.vocab = {}

    def gather_info(self):
        # initialize vocab
        for chap in self:
            for unit in chap:
                for word in unit:
                    self.vocab[word.word] = word

    def extract_english(self, word):
        return filter(lambda x: x in string.ascii_letters, word).strip()

    def contains_word(self, word):
        word = self.extract_english(word)
        return (word in self.vocab.keys())

    def contains_word_in_sentence(self, word):
        words = word.split(" ")
        for w in words:
            if self.contains_word(w):
                return True
        return False

    @staticmethod
    def fromObj(obj):
        book = VBook()
        tmp = []
        for i in range(len(obj)):
            if len(tmp) and obj[i]["cid"] != tmp[0]["cid"]:
                book.chaps.append(VChap.fromObj(tmp, book))
                tmp = [obj[i]]
            else:
                tmp.append(obj[i])
        book.chaps.append(VChap.fromObj(tmp, book))
        book.gather_info()
        return book

    def __iter__(self):
        return self.chaps.__iter__()

    def __getitem__(self, item):
        if type(item) is types.IntType:
            if item <= 0: raise KeyError
            return self.chaps[item - 1]
        if type(item) is types.SliceType:
            if item.start <= 0: raise KeyError
            return self.chaps[item.start - 1 : item.stop]
        raise KeyError


__author__ = 'badpoet'

from .vword import VWord
import types

class VUnit(object):

    def __init__(self, book):
        self.book = book
        self.chap_id = -1
        self.unit_id = -1
        self.words = []

    @staticmethod
    def fromObj(obj, book):
        unit = VUnit(book)
        unit.chap_id = obj[0]["cid"]
        unit.unit_id = obj[0]["uid"]
        unit.words = [VWord.fromDict(e, book) for e in obj]
        return unit

    def get_word(self, word):
        return self.words[word - 1]

    def __iter__(self):
        return self.words.__iter__()

    def __getitem__(self, item):
        if type(item) is types.IntType:
            return self.words[item - 1]
        if type(item) is types.SliceType:
            return self.words[item.start - 1 : item.stop]
        raise KeyError

    def all_words(self):
        return self.words

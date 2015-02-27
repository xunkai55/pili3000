__author__ = 'badpoet'

from .vterm import VTerm
import types

class VWord(object):

    def __init__(self, book):
        self.book = book
        self.word = ""
        self.desc = ""
        self.chap_id = -1
        self.unit_id = -1
        self.word_id = -1
        self.meanings = []

    @staticmethod
    def fromDict(dic, book):
        word = VWord(book)
        word.word = dic["word"]
        word.desc = dic["desc"]
        word.chap_id = dic["cid"]
        word.unit_id = dic["uid"]
        word.word_id = dic["gid"]
        word.meanings = [VTerm.fromDict(e, book) for e in dic["meanings"]]
        return word

    def id_tuple(self):
        return (self.chap_id, self.unit_id, self.word_id)

    def __iter__(self):
        return self.meanings.__iter__()

    def __getitem__(self, item):
        if type(item) is types.IntType:
            return self.meanings[item - 1]
        if type(item) is types.SliceType:
            return self.meanings[item.start - 1 : item.stop]
        raise KeyError


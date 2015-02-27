__author__ = 'badpoet'

from .vunit import VUnit
import types

class VChap(object):

    def __init__(self, book):
        self.units = []
        self.chap_id = -1
        self.book = book

    @staticmethod
    def fromObj(obj, book):
        chap = VChap(book)
        chap.chap_id = obj[0]["cid"]
        tmp = []
        for i in range(len(obj)):
            if len(tmp) and obj[i]["uid"] != tmp[0]["uid"]:
                chap.units.append(VUnit.fromObj(tmp, book))
                tmp = [obj[i]]
            else:
                tmp.append(obj[i])
        chap.units.append(VUnit.fromObj(tmp, book))
        return chap

    def __iter__(self):
        return self.units.__iter__()

    def __getitem__(self, item):
        if type(item) is types.IntType:
            return self.units[item - 1]
        if type(item) is types.SliceType:
            return self.units[item.start - 1 : item.stop]
        raise KeyError

    def all_words(self):
        t = []
        for unit in self.units:
            t.extend(unit.all_words())
        return t
__author__ = "badpoet"

from .pili3000.model.vocab.vchap import VChap

class VBook(object):

    def __init__(self):
        self.chaps = []
        self.title = "GRE 3000"

    @staticmethod
    def fromObj(obj):
        book = VBook()
        tmp = []
        for i in range(len(obj) + 1):
            if i == len(obj) or (len(tmp) and obj[i]["cid"] != tmp[0]["cid"]):
                book.chaps.append(VChap.fromObj(tmp))
                tmp = []
            else:
                tmp.append(obj[i])
        return book

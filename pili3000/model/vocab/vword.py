__author__ = 'badpoet'

from .pili3000.model.vocab.vterm import VTerm

class VWord(object):

    def __init__(self):
        self.word = ""
        self.desc = ""
        self.chap_id = -1
        self.unit_id = -1
        self.global_id = -1
        self.meanings = []

    @staticmethod
    def fromDict(dic):
        word = VWord()
        word.word = dic["word"]
        word.desc = dic["desc"]
        word.chap_id = dic["cid"]
        word.unit_id = dic["uid"]
        word.global_id = dic["gid"]
        print word.global_id
        word.meanings = [VTerm.fromDict(e) for e in dic["meanings"]]
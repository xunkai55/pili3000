__author__ = 'badpoet'

from .pili3000.model.vocab.vword import VWord

class VUnit(object):

    def __init__(self):
        self.chap_id = -1
        self.unit_id = -1
        self.words = []

    @staticmethod
    def fromObj(obj):
        unit = VUnit()
        unit.chap_id = obj[0]["cid"]
        unit.unit_id = obj[0]["uid"]
        unit.words = [VWord.fromDict(e) for e in obj]
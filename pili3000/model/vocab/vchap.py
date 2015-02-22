__author__ = 'badpoet'

from .pili3000.model.vocab.vunit import VUnit

class VChap(object):

    def __init__(self):
        self.units = []
        self.chap_id = -1

    @staticmethod
    def fromObj(obj):
        chap = VChap()
        chap.chap_id = obj[0]["cid"]
        tmp = []
        for i in range(len(obj) + 1):
            if i == len(obj) or (len(tmp) and obj[i]["uid"] != tmp[0]["uid"]):
                chap.units.append(VUnit.fromObj(tmp))
                tmp = []
            else:
                tmp.append(obj[i])

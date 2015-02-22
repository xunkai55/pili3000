__author__ = 'badpoet'

class VTerm(object):

    def __init__(self):
        self.homo = []
        self.anto = []
        self.syno = []
        self.explanation = ""
        self.example = ""

    @staticmethod
    def fromDict(dic):
        term = VTerm()
        term.homo = dic["homo"]
        term.anto = dic["anto"]
        term.syno = dic["syno"]
        term.explanation = dic.get("explanation", "")
        term.example = dic.get("example", "")
        return term

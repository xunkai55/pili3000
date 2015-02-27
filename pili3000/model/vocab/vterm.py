# -*- coding: utf-8 -*-
__author__ = 'badpoet'

import types

class VTerm(object):

    def __init__(self, book):
        self.book = book
        self.homo_raw = []
        self.anto_raw = []
        self.syno_raw = []
        self.homo = ""
        self.anto = ""
        self.syno = ""
        self.explanation = ""
        self.example = ""

    @staticmethod
    def fromDict(dic, book):
        term = VTerm(book)
        term.homo_raw = dic["homo"]
        term.anto_raw = dic["anto"]
        term.syno_raw = dic["syno"]
        term.homo = u"[近] " + ", ".join(dic["homo"]) if dic["homo"] else ""
        term.anto = u"[反] " + ", ".join(dic["anto"]) if dic["anto"] else ""
        term.syno = u"[同] " + ", ".join(dic["syno"]) if dic["syno"] else ""
        term.explanation = dic.get("explanation", "")
        term.example = u"[例] " + dic.get("example", "") if dic.get("example", "") else ""
        return term



# -*- coding: utf-8 -*-

__author__ = 'badpoet'

from termview import TermView
from pili3000.model import g3000

class DicView(TermView):

    def __init__(self):
        super(DicView, self).__init__("dic")
        self.info(u"输入三个整数（章节，单元，序号）以查询单词")

    def run(self):
        while True:
            cid, uid, wid = (0, 0, 0)
            try:
                cid, uid, wid = map(int, self.accept_command().split())
            except ValueError, e:
                self.hint(u"输入三个整数（章节，单元，序号）以查询单词")
            try:
                w = g3000[cid][uid][wid]
                self.red_star()
                self.yellow(w.word)
                for t in w:
                    self.green(t.explanation)
                    self.out(t.example)
                    self.out(t.homo)
                    self.out(t.anto)
                    self.out(t.syno)
            except (KeyError, IndexError), e:
                print "Invalid id(s)"

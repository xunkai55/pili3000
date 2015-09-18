# -*- coding: utf-8 -*-

__author__ = 'badpoet'

from termview import TermView
from pili3000.model import g3000

class DicView(TermView):

    def __init__(self):
        super(DicView, self).__init__("dic")
        self.info(u"输入三个整数（章节，单元，序号）以查询单词，或直接输入单词查询")

    def run(self):
        while True:
            cid, uid, wid = (0, 0, 0)
            x = self.accept_command()
            try:
                cid, uid, wid = map(int, x.split())
            except ValueError, e:  # input a word
                try:
                    w = x.lower()
                    word = g3000.vocab[w]
                    self.out_word(word, highlight_learned_only = False)
                except KeyError, e:
                    self.alert("Can not find the word")
            else:
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
                    self.alert("Invalid id(s)")

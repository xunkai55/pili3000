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
                    self.red_star()
                    self.magenta(word.word)
                    for m in word:
                        self.yellow(m.explanation)
                        self.out(m.example)
                        links = [(u"[同] ", m.syno_raw), (u"[近] ", m.homo_raw), (u"[反] ", m.anto_raw)]
                        for item, content in links:
                            if not content: continue
                            self.out_(item)
                            for each in content:
                                if g3000.contains_word_in_sentence(each):  # (4, 5, 2)
                                    self.blue_(each)
                                else:
                                    self.out_(each)
                                self.out_("; ")
                            self.endl()
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

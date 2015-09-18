# -*- coding: utf-8 -*-

__author__ = 'badpoet'

from termview import TermView
from pili3000.model import g3000
from random import shuffle

class LearnView(TermView):

    def __init__(self, chap_id):
        super(LearnView, self).__init__("learn")
        self.chap_id = chap_id
        self.alert(
            u"开始学习第%d个List" % self.chap_id
        )

    def run(self):
        NO_FOWARD_LINK = False
        chap_terms = []
        for unit in g3000[self.chap_id]:
            self.hint(u"学习第%d单元。j跳过" % unit.unit_id)
            learning_flag = True
            if self.accept_command() == "j":
                learning_flag = False
            unit_terms = []
            for word in unit:
                for term in word.meanings + word.derivatives:
                    unit_terms.append((term, word.word))
                    if learning_flag:
                        self.out_word(word, highlight_learned_only=True)
                        self.validate_input(word.word, 3)
            self.hint(u"通过例子复习。j跳过")
            reviewing_flag = True
            if self.accept_command() == "j":
                reviewing_flag = False
            shuffle(unit_terms)
            for term, word in unit_terms:
                if not term.example:
                    continue
                if reviewing_flag:
                    self.yellow(term.example)
                    self.validate_input(word, 3)
                    self.out(term)
            chap_terms.extend(unit_terms)
        self.hint(u"浏览本单元单词。j跳过")
        if self.accept_command() != "j":
            for term, word in chap_terms:
                self.yellow(word)
                self.accept_command()
                self.out(term)
        self.hint(u"学习完成。Congratulations！请使用review模式巩固学习成果")


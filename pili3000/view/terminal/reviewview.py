# -*- coding: utf-8 -*-

__author__ = 'badpoet'

from termview import TermView
from pili3000.model import g3000
from random import shuffle, sample

class ReviewView(TermView):

    def __init__(self, chap_id):
        super(ReviewView, self).__init__("review")
        self.chap_id = chap_id
        self.alert(
            u"开始复习第%d个List" % self.chap_id
        )

    def run(self):
        while True:
            self.info(u"输入E使用例子复习，M使用含义复习，C使用英汉选择题复习。若采用局部复习，请增加P选项（如EP）")
            x = self.accept_command()
            try:
                partial = x.find("P") >= 0
                if x.find("E") >= 0:
                    self.run_example_review(partial)
                elif x.find("M") >= 0:
                    self.run_meaning_review(partial)
                elif x.find("C") >= 0:
                    self.run_choice_review(partial)
                else:
                    self.alert("Cannot parse your command")
            except KeyboardInterrupt, e:
                print
                self.alert("Interrupted")

    def run_review(self, partial, content):
        t = []
        for word in g3000[self.chap_id].all_words():
            t.extend([(word.word, content(meaning)) for meaning in word if content(meaning)])
        shuffle(t)
        if partial:
            t = t[ : int(0.2 * len(t))]
        tot = len(t)
        now = 0
        cnt = 0
        self.hint(u"复习开始")
        for w, c in t:
            now += 1
            self.red_star()
            self.yellow(c)
            if self.validate_input(w, 3):
                cnt += 1
            self.out("%d/%d/%d" % (cnt, now, tot))
        self.hint(u"复习完成。Congratulations！你的正确率是：", cnt * 100.0 / tot)

    def run_example_review(self, partial):
        self.run_review(partial, lambda x: x.example)

    def run_meaning_review(self, partial):
        self.run_review(partial, lambda x: x.explanation)

    def run_choice_review(self, partial):
        CHOICE_NUM = 5
        ALPHA = ["A", "B", "C", "D", "E"]
        t = []
        for word in g3000[self.chap_id].all_words():
            t.extend([(word.word, meaning.explanation) for meaning in word if meaning.explanation])
        shuffle(t)
        if partial:
            t = t[ : int(0.2 * len(t))]
        tot = len(t)
        now = 0
        cnt = 0
        self.hint(u"复习开始")
        for word, answer in t:
            answer_set = {(word, answer)}
            while len(answer_set) < CHOICE_NUM:
                answer_set |= set(
                    filter(
                        lambda x: x[0] != word,
                        sample(t, CHOICE_NUM - len(answer_set))
                    )
                )
            c = list(answer_set)
            shuffle(c)
            self.red_star()
            self.yellow(word)
            for i in range(len(c)):
                self.item(ALPHA[i])
                self.out(c[i][1])
            answer_index = c.index((word, answer))
            state = self.validate_input(ALPHA[answer_index], 1)
            for i in range(len(c)):
                if i == answer_index:
                    if state:
                        self.green(c[i][0], c[i][1])
                        cnt += 1
                    else:
                        self.red(c[i][0], c[i][1])
                else:
                    self.out(c[i][0], c[i][1])
            now += 1
            self.out("%d/%d/%d" % (cnt, now, tot))

        self.hint(u"复习完成。Congratulations！你的正确率是：", cnt * 100.0 / tot)


# -*- coding: utf-8 -*-

__author__ = 'badpoet'

from termcolor import colored

from pili3000.model import g3000

DEBUG = True

class TermView(object):

    def __init__(self, mode):
        self.header = "[pili" + "-" + mode + "] "
        self.ps_color = "blue"
        self.ps = ">>"

    def show_ps(self, wrong = False):
        if wrong:
            print colored("X ", "red"),
        print colored(self.ps, self.ps_color),

    def show_message(self, color, *args):
        msg = self.header + " ".join(map(unicode, args))
        print colored(msg, color)

    def info(self, *args):
        self.show_message("white", *args)

    def hint(self, *args):
        self.show_message("green", *args)

    def alert(self, *args):
        self.show_message("red", *args)

    def colored(self, color, *args):
        s = " ".join(map(unicode, args)).strip()
        if s: print colored(s, color)

    def yellow(self, *args):
        self.colored("yellow", *args)

    def red(self, *args):
        self.colored("red", *args)

    def green(self, *args):
        self.colored("green", *args)

    def magenta(self, *args):
        self.colored("magenta", *args)

    def blue(self, *args):
        self.colored("blue", *args)

    def red_star(self):
        print colored("*", "red"),

    def item(self, item):
        print colored(item + " ", "red"),

    def out(self, *args):
        s = " ".join(map(unicode, args)).strip()
        if s: print s

    def endl(self):
        print

    def out_word(self, word, highlight_learned_only):
        self.red_star()
        self.magenta(word.word)
        for m in word:
            self.yellow(m.explanation)
            self.out(m.example)
            links = [(u"[同] ", m.syno_raw), (u"[近] ", m.homo_raw), (u"[反] ", m.anto_raw)]
            for item, content in links:
                if not content: continue
                self.out(item)
                for each in content:
                    if g3000.contains_word_in_sentence(each) and (not highlight_learned_only or each < word):  # (4, 5, 2)
                        self.blue(each)
                    else:
                        self.out(each)
                    self.out("; ")
                self.endl()

    def validate_input(self, content = "", counter = -1):
        try:
            wrong = False
            while counter:
                self.show_ps(wrong)
                x = raw_input()
                if x == content:
                    return True
                wrong = True
                counter -= 1
            if counter == 0:  # try but fail
                self.magenta("Correct answer: ", content)
            return False
        except EOFError, e:
            if DEBUG:
                return True
            else:
                raise e

    def accept_command(self, wrong = False):
        self.show_ps(wrong)
        return raw_input()


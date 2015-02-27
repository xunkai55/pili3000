__author__ = 'badpoet'

from termview import TermView
from learnview import LearnView
from dicview import DicView
from reviewview import ReviewView

class MainView(TermView):

    def __init__(self):
        super(MainView, self).__init__("main")
        self.ps_color = "cyan"
        self.ps = "pili-console$"

    def run(self):
        while True:
            view = None
            try:
                x = self.accept_command().split()
                if x[0] == "learn":
                    view = LearnView(int(x[1]))
                elif x[0] == "review":
                    view = ReviewView(int(x[1]))
                elif x[0] == "dic":
                    view = DicView()
                elif x[0] == "exit" or x[0] == "quit":
                    raise KeyboardInterrupt
            except KeyboardInterrupt, e:
                print
                self.info("Bye")
                break
            except Exception, e:
                self.alert("Cannot parse your command")
                continue
            if not view:
                self.alert("No such mode")
                continue
            try:
                view.run()
            except KeyboardInterrupt, e:
                print

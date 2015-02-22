__author__ = 'badpoet'

from projector import Projector

class BProjector(Projector):

    def __init__(self, chap, unit = 0):
        super(BProjector).__init__()
        self.v_chap_id = chap
        self.v_unit_id = unit
        self.random = False

    def get_slide(self):
        pass

    def next_slide(self):
        pass
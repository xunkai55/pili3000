__author__ = 'badpoet'

class Projector(object):

    def __init__(self):
        self.slide_lock = False
        pass

    def get_slide(self):
        '''
        Get the current slide. If there is no slides, "None" will be returned.
        :return: The current slide. See @model.slide
        '''
        pass

    def next_slide(self):
        '''
        Move the cursor to the next slide and return the new slide.
        :return: The new (previously "next") slide
        '''
        pass

    def unlock_slide(self):
        self.slide_lock = False

    def lock_slide(self):
        self.slide_lock = True

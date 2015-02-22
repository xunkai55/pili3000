__author__ = 'badpoet'

class ContentItem(object):

    def __init__(self, header, content):
        self.header = header
        self.content = content

class Slide(object):

    def __init__(self, title, contents):
        '''
        Create a slide from scratch.
        :param title: (string) The title of this slide.
        :param contents: (list(dict("header", "content"))) A list of contents, each of which consists a header and a content.
        '''
        self.title = title
        self.contents = [ContentItem(e.get("header", ""), e.get("content", "")) for e in contents]

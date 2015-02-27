__author__ = 'badpoet'

import json

from .vocab.vbook import VBook

# TODO configurable data path
g3000 = VBook.fromObj(json.load(open("obj.json", "r")))


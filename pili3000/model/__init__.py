__author__ = 'badpoet'

import json

from .pili3000.model.vocab.vbook import VBook

# TODO configurable data path
g3000 = VBook.fromObj(json.load(open("../obj.json", "r")))


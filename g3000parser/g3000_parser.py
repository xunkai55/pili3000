# -*- coding: utf-8 -*-

import codecs
from string import Template
import re

alphabet = u'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
alphabet2 = u'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '

def split_words(line):
    res = line.split(u",")
    seps = [u";", u"；", u"，"]
    for sep in seps:
        res_bak = res
        res = []
        for each in res_bak:
            res.extend(each.split(sep))
    return res


def MeaningDict(tmp):

    self = {}
    lines = tmp.split("\n")
    self["syno"] = []
    self["anto"] = []
    self["homo"] = []
    for each in lines:
        line = each.strip()
        if len(line) == 0:
            continue
        if line.find(u"考法") >= 0:
            con = re.sub(u"【.*?】", "", line)
            self["explanation"] = con.strip()
            continue
        if line.find(u"【派") >= 0:
            self["explanation"] = line.strip()
            continue
        if line.find(u"【例") >= 0:
            con = re.sub(u"【.*?】", "", line)
            self["example"] = con.strip()
            continue
        if line.find(u"【同") >= 0:
            con = re.sub(u"【.*?】", "", line)
            words = split_words(con)
            for ew in words:
                rew = ""
                for ec in ew:
                    if alphabet2.find(ec):
                        rew += ec
                if len(rew.strip()):
                    self["syno"].append(rew.strip())
            continue
        if line.find(u"【近") >= 0:
            con = re.sub(u"【.*?】", "", line)
            words = split_words(con)
            for ew in words:
                rew = ""
                for ec in ew:
                    if alphabet2.find(ec):
                        rew += ec
                if len(rew.strip()):
                    self["homo"].append(rew.strip())
            continue
        if line.find(u"【反") >= 0:
            con = re.sub(u"【.*?】", "", line)
            words = split_words(con)
            for ew in words:
                rew = ""
                for ec in ew:
                    if alphabet2.find(ec):
                        rew += ec
                if len(rew.strip()):
                    self["anto"].append(rew.strip())
            continue
        print line

    return self

def WordObj(w, desc, cid, uid, gid):

    self = {}
    w = re.sub(u"\\[.*?\\]", "", w)
    self["word"] = w.strip()
    self["desc"] = desc[:].strip()
    lines = desc.split('\n')
    self["meanings"] = []
    self["derv"] = []
    self["cid"] = cid
    self["uid"] = uid
    self["gid"] = gid

    tmp = ""
    is_derv = False
    for each in lines:
        line = each.strip()
        if len(line) == 0:
            continue
        if line.find(u"考法") >= 0 or line.find(u"【派") >= 0:
            if len(tmp):
                if not is_derv:
                    self["meanings"].append(MeaningDict(tmp))
                else:
                    self["derv"].append(MeaningDict(tmp))
            if line.find(u"【派") >= 0:
                is_derv = True
            else:
                is_derv = False
            tmp = line[:] + "\n"
        else:
            tmp += line[:] + "\n"
    if len(tmp):
        if not is_derv:
            self["meanings"].append(MeaningDict(tmp))
        else:
            self["derv"].append(MeaningDict(tmp))
    return self

f = codecs.open("g3000.txt", "r", "utf-8")
txt = f.read()
f.close()

lines = txt.split('\n')

list_id = 0
unit_id = 0
word_id = 1
g_word_id = 0
w = ""
desc = ""
tar = []
storage = []

for i in range(len(lines)):
    line = lines[i].strip()

    if len(line) == 0:
        continue

    if alphabet.find(line[0]) >= 0:

        # List
        if line.find(u"List") == 0:
            if w:
                word_id += 1
                storage.append((w, desc, list_id, unit_id, word_id))
                g_word_id += 1
                w = ""
                desc = ""
            list_id += 1
            unit_id = 0
            word_id = 1
            if (list_id >= 28):
                tar.append(line)
            continue

        # Unit
        if line.find(u"Unit") == 0:
            if w:
                word_id += 1
                storage.append((w, desc, list_id, unit_id, word_id))
                g_word_id += 1
                w = ""
                desc = ""

            unit_id += 1
            word_id = 1
            if (list_id >= 28):
                tar.append(line)
            continue

        # Word
        tar.append("zxk")
        if w:
            word_id += 1
            storage.append((w, desc, list_id, unit_id, word_id))
            g_word_id += 1
        w = line[:]
        desc = ""

    else:

        desc += line[:] + '\n'
        
word_id += 1
storage.append((w, desc, list_id, unit_id, word_id))
g_word_id += 1
print (list_id, unit_id, word_id)
print g_word_id

# make pool

import json

tot = []

import codecs

for each in storage:
    obj = WordObj(each[0], each[1], each[2], each[3], each[4] - 1)
    tot.append(obj)

f = codecs.open("../obj.json", "w", "utf-8")
json.dump(tot, f, ensure_ascii = False)
f.close()

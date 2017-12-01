import re


def blank(oLine):

    if re.match('^\s*$', oLine.line):
        oLine.isBlank = True

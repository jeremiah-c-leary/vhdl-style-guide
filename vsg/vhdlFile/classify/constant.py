import re


def constant(dVars, oLine):

    if re.match('^\s*constant', oLine.lineLower):
        oLine.isConstant = True
        oLine.indentLevel = 1

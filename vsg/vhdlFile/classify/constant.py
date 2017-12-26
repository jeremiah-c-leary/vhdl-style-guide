import re


def constant(dVars, oLine):

    if re.match('^\s*constant', oLine.lineLower) and not oLine.insideFunction:
        oLine.isConstant = True
        oLine.indentLevel = 1

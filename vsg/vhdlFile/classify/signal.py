import re


def signal(dVars, oLine):

    if re.match('^\s*signal', oLine.lineLower) and not oLine.insideFunction:
        oLine.isSignal = True
        oLine.indentLevel = 1

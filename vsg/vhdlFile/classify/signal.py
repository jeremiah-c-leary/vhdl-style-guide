import re


def signal(dVars, oLine):

    if re.match('^\s*signal', oLine.lineLower):
        oLine.isSignal = True
        oLine.indentLevel = 1

import re


def forLoop(dVars, oLine):

    if re.match('^\s*for\s.*\sin\s.*\sloop', oLine.lineLower):
        oLine.isForLoopKeyword = True
        oLine.insideForLoop = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if re.match('^\s*end\s+loop', oLine.lineLower):
        oLine.isForLoopEnd = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']

import re


def function(dVars, oLine):

    if re.match('^\s*function\s', oLine.lineLower) or re.match('^\s*impure\s', oLine.lineLower):
        oLine.isFunctionKeyword = True
        oLine.insideFunction = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideFunction:
        if re.match('^\s*begin', oLine.lineLower):
            oLine.isFunctionBegin = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
        if re.match('^\s*return', oLine.lineLower):
            oLine.isFunctionReturn = True
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and not oLine.isEndCaseKeyword and not oLine.isForLoopEnd:
            oLine.isFunctionEnd = True
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iCurrentIndentLevel'] -= 1

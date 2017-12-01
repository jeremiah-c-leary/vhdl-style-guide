import re


def type(dVars, oLine):

    if re.match('^\s*type\s', oLine.lineLower):
        oLine.isTypeKeyword = True
        oLine.insideType = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideType:
        if not oLine.isTypeKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if ';' in oLine.line:
            oLine.isTypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            if re.match('^\s*\)\s*;', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel']

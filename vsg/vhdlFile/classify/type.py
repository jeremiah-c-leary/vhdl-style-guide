import re


def type(dVars, oLine):

    if re.match('^\s*type\s+\w+\s+is\s+array', oLine.line, re.IGNORECASE):
        oLine.isTypeKeyword = True
        oLine.isTypeArrayKeyword = True
        oLine.insideTypeArray = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    elif re.match('^\s*type\s', oLine.line, re.IGNORECASE):
        oLine.isTypeKeyword = True
        oLine.insideType = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideTypeArray:
        if ';' in oLine.line:
            oLine.isTypeArrayEnd = True
            oLine.isTypeEnd = True
    if oLine.insideType:
        if not oLine.isTypeKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if ';' in oLine.line:
            oLine.isTypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            if re.match('^\s*\)\s*;', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel']

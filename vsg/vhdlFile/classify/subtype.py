import re


def subtype(dVars, oLine):

    if re.match('^\s*subtype\s', oLine.line, re.IGNORECASE):
        oLine.isSubtypeKeyword = True
        oLine.insideSubtype = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideSubtype:
        if not oLine.isSubtypeKeyword and not oLine.isBlank:
            oLine.indentLevel = dVars['iCurrentIndentLevel']
        if ';' in oLine.line:
            oLine.isSubtypeEnd = True
            dVars['iCurrentIndentLevel'] -= 1
            if re.match('^\s*\)\s*;', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel']

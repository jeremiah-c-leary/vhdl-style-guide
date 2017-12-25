import re


def attribute(dVars, oLine):

    if re.match('^\s*attribute', oLine.line, re.IGNORECASE):
        oLine.isAttributeKeyword = True
        oLine.insideAttribute = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideAttribute and not oLine.isAttributeKeyword:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideAttribute = True
    if oLine.insideAttribute and ';' in oLine.line:
        oLine.isAttributeEnd = True
        dVars['iCurrentIndentLevel'] -= 1

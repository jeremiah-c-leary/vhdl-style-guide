import re


def generic(dVars, oLine):
    if re.match('^\s*generic', oLine.lineLower) and not oLine.insideGenericMap:
        oLine.isGenericKeyword = True
        oLine.insideGenericMap = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideGenericMap:
        if re.match('^\s*\S+.*:', oLine.line):
            oLine.isGenericDeclaration = True
            if not oLine.isGenericKeyword:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iOpenParenthesis'] += oLine.line.count('(')
        dVars['iCloseParenthesis'] += oLine.line.count(')')
        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iOpenParenthesis'] = 0
            dVars['iCloseParenthesis'] = 0
            oLine.isEndGenericMap = True
            dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 2

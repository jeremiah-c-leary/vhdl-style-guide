import re


def generic(dVars, oLine):
    if not (oLine.insideEntity or oLine.insideComponent):
        return
    if re.match('^\s*generic', oLine.lineNoComment, re.IGNORECASE) and not oLine.insideGenericMap:
        oLine.isGenericKeyword = True
        oLine.insideGenericMap = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
        if '(' not in oLine.lineNoComment:
            return

    if oLine.insideGenericMap:
        if re.match('^\s*\S+.*:', oLine.lineNoComment):
            oLine.isGenericDeclaration = True
            if not oLine.isGenericKeyword:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
        dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')
        if dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
            oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            dVars['iOpenParenthesis'] = 0
            dVars['iCloseParenthesis'] = 0
            oLine.isEndGenericMap = True
            dVars['iCurrentIndentLevel'] = dVars['iCurrentIndentLevel'] - 2

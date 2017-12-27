import re


def procedure(dVars, oLine):

    if re.match('^\s*procedure\s', oLine.lineLower):
        oLine.isProcedureKeyword = True
        oLine.insideProcedure = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideProcedure:
        dVars['iOpenParenthesis'] += oLine.lineNoComment.count('(')
        dVars['iCloseParenthesis'] += oLine.lineNoComment.count(')')
        if re.match('^.*\w+\s*:\s*\w+', oLine.line):
            oLine.isProcedureParameter = True
            if not oLine.isProcedureKeyword:
                oLine.indentLevel = dVars['iCurrentIndentLevel']
        if oLine.insidePackage:
            if ';' in oLine.line and dVars['iOpenParenthesis'] == dVars['iCloseParenthesis']:
                dVars['iOpenParenthesis'] = 0
                dVars['iCloseParenthesis'] = 0
                oLine.isProcedureEnd = True
                dVars['iCurrentIndentLevel'] -= 1
        else:
            if re.match('^\s*begin', oLine.lineLower):
                oLine.isProcedureBegin = True
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            if re.match('^\s*end', oLine.lineLower) and not oLine.isEndIfKeyword and \
               not oLine.isEndCaseKeyword and not oLine.isForLoopEnd and not oLine.isWhileLoopEnd:
                oLine.isProcedureEnd = True
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                dVars['iCurrentIndentLevel'] -= 1
                dVars['iOpenParenthesis'] = 0
                dVars['iCloseParenthesis'] = 0

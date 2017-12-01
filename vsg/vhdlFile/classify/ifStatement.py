import re


def ifStatement(dVars, oLine):

    if re.match('^\s*if', oLine.lineLower):
        oLine.isIfKeyword = True
        oLine.insideIf = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if re.match('^\s*elsif', oLine.lineLower) or re.match('^.*\selsif', oLine.lineLower):
        oLine.isElseIfKeyword = True
        oLine.insideIf = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
    if oLine.insideIf and 'then' in oLine.lineLower:
        oLine.isThenKeyword = True
    if re.match('^\s*else', oLine.lineLower) or re.match('^.*\selse', oLine.lineLower):
        oLine.isElseKeyword = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
    if re.match('^\s*end\s+if', oLine.lineLower) or re.match('^.*\send\s+if', oLine.lineLower):
        oLine.isEndIfKeyword = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']

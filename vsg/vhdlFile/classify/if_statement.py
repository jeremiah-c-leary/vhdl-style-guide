import re


def if_statement(dVars, oLine):
    if not (oLine.insideProcess or oLine.insideFunction or oLine.insideProcedure):
        return

    if re.match('^\s*if', oLine.lineNoComment, re.IGNORECASE):
        oLine.isIfKeyword = True
        oLine.insideIf = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if re.match('^\s*elsif', oLine.lineNoComment, re.IGNORECASE) or re.match('^.*[\s|;]elsif', oLine.lineNoComment, re.IGNORECASE):
        oLine.isElseIfKeyword = True
        oLine.insideIf = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
    if oLine.insideIf and 'then' in oLine.lineLower:
        oLine.isThenKeyword = True
    if re.match('^\s*else', oLine.lineNoComment, re.IGNORECASE) or re.match('^.*[\s|;]else', oLine.lineNoComment, re.IGNORECASE):
        oLine.isElseKeyword = True
        oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
    if re.match('^\s*end\s+if', oLine.lineNoComment, re.IGNORECASE) or re.match('^.*[\s|;]end\s+if', oLine.lineNoComment, re.IGNORECASE):
        oLine.isEndIfKeyword = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']

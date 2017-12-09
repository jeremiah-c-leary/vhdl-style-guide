import re


def while_loop(dVars, oLine):

    if re.match('^\s*while\s.*\sloop', oLine.line, re.IGNORECASE):
        oLine.isWhileLoopKeyword = True
        oLine.insideWhileLoop = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if re.match('^\s*end\s+loop', oLine.line, re.IGNORECASE) and oLine.insideWhileLoop:
        oLine.isWhileLoopEnd = True
        dVars['iCurrentIndentLevel'] -= 1
        oLine.indentLevel = dVars['iCurrentIndentLevel']

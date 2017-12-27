import re


def constant(dVars, oLine):

    if re.match('^\s*constant', oLine.lineLower) and \
       not oLine.insideFunction and not oLine.insideProcedure:
        oLine.isConstant = True
        oLine.indentLevel = 1
        oLine.insideConstant = True
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideConstant:
        if ';' in oLine.line:
            dVars['iCurrentIndentLevel'] -= 1
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.isConstantEnd = True
        elif not oLine.isConstant:
            if re.match('^\s*\(', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
            else:
                oLine.indentLevel = dVars['iCurrentIndentLevel']

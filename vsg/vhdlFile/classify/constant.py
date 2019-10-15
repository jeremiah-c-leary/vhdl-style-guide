import re


def constant(dVars, oLine, oLinePrevious):

    if re.match('^\s*constant', oLine.lineLower) and \
       not oLine.insideFunction and not oLine.insideProcedure and \
       not oLine.insideConcurrent:
        oLine.isConstant = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        oLine.insideConstant = True
        dVars['iCurrentIndentLevel'] += 1
        if re.match('^.*:=\s*\(', oLine.lineNoComment):
            dVars['fConstantArray'] = True
    if oLine.insideConstant:
        if ';' in oLine.line:
            dVars['iCurrentIndentLevel'] -= 1
            oLine.indentLevel = dVars['iCurrentIndentLevel']
            oLine.isConstantEnd = True
            if dVars['fConstantArray']:
                oLine.isConstantArray = True
            dVars['fConstantArray'] = False
        elif not oLine.isConstant:
            if re.match('^\s*\(', oLine.line):
                oLine.indentLevel = dVars['iCurrentIndentLevel'] - 1
                dVars['fConstantArray'] = True
                oLinePrevious.isConstantArray = True
            else:
                oLine.indentLevel = dVars['iCurrentIndentLevel']

    if dVars['fConstantArray']:
        oLine.isConstantArray = True


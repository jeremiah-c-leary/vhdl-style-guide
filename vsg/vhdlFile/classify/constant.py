import re


def constant(self, dVars, lTokens, lObjects, oLine, oLinePrevious):
    '''
    constant identifier_list : subtype_indication [ := expression ] ;
    '''

    if re.match('^\s*constant', oLine.lineLower) and \
       not oLine.insideProcedure and \
       not oLine.insideConcurrent:
        if oLine.insideFunction:
            if not dVars['fFunctionBeginDetected'] and dVars['fFunctionReturnTypeDetected']:
                oLine.isConstant = True
                oLine.indentLevel = dVars['iCurrentIndentLevel']
                oLine.insideConstant = True
                dVars['iCurrentIndentLevel'] += 1
                if re.match('^.*:=\s*\(', oLine.lineNoComment):
                    dVars['fConstantArray'] = True
        else: 
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

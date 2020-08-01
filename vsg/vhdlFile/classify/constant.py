import re

from vsg import parser


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


    for iToken, sToken in enumerate(lTokens):
        if not dVars['bConstantKeywordFound']:

            classify_constant_keyword(sToken, iToken, lObjects, dVars)

        else:

            if not dVars['bConstantColonFound']:
                classify_colon(sToken, iToken, lObjects, dVars)
                classify_comma(sToken, iToken, lObjects)
                classify_constant_identifier(sToken, iToken, lObjects)
            else:
                if not dVars['bConstantAssignmentOperatorFound']:
                    classify_assignment_operator(sToken, iToken, lObjects, dVars)
                    classify_constant_subtype_indication(sToken, iToken, lObjects)
                else:
                    classify_constant_assignment_expression(sToken, iToken, lObjects)
                classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_constant_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'constant':
        lObjects[iToken] = parser.constant_keyword(sToken)
        dVars['bConstantKeywordFound'] = True 


def classify_constant_identifier(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':' and sToken != ',':
        lObjects[iToken] = parser.constant_identifier(sToken)


def classify_comma(sToken, iToken, lObjects):
    if sToken == ',':
        lObjects[iToken] = parser.constant_comma()


def classify_colon(sToken, iToken, lObjects, dVars):
    if sToken == ':':
        lObjects[iToken] = parser.constant_colon()
        dVars['bConstantColonFound'] = True

def classify_constant_subtype_indication(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':=':
        lObjects[iToken] = parser.constant_subtype_indication(sToken)

def classify_assignment_operator(sToken, iToken, lObjects, dVars):
    if sToken == ':=':
        lObjects[iToken] = parser.constant_assignment_operator()
        dVars['bConstantAssignmentOperatorFound'] = True

def classify_constant_assignment_expression(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ';':
        lObjects[iToken] = parser.constant_assignment_expression(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.constant_semicolon()
        dVars['bConstantKeywordFound'] = False
        dVars['bConstantColonFound'] = False
        dVars['bConstantAssignmentOperatorFound'] = False


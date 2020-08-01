import re

from vsg import parser


def variable(self, dVars, lTokens, lObjects, oLine):
    '''
    [ shared ] variable identifer_list : subtype_indication [ := expression ]
    '''

    if re.match('^\s*variable', oLine.lineLower):
        oLine.isVariable = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bVariableKeywordFound']:

            classify_keyword(sToken, iToken, lObjects, dVars)
            classify_shared(sToken, iToken, lObjects, dVars)

        else:

            if not dVars['bVariableColonFound']:
                classify_colon(sToken, iToken, lObjects, dVars)
                classify_comma(sToken, iToken, lObjects)
                classify_identifier(sToken, iToken, lObjects)
            else:
                if not dVars['bVariableAssignmentOperatorFound']:
                    classify_assignment_operator(sToken, iToken, lObjects, dVars)
                    classify_subtype_indication(sToken, iToken, lObjects)
                else:
                    classify_assignment_expression(sToken, iToken, lObjects)
                classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_shared(sToken, iToken, lObjects, dVars):
    if sToken == 'shared':
        lObjects[iToken] = parser.variable_shared_keyword(sToken)


def classify_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'variable':
        lObjects[iToken] = parser.variable_keyword(sToken)
        dVars['bVariableKeywordFound'] = True 


def classify_identifier(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':' and sToken != ',':
        lObjects[iToken] = parser.variable_identifier(sToken)


def classify_comma(sToken, iToken, lObjects):
    if sToken == ',':
        lObjects[iToken] = parser.variable_comma()


def classify_colon(sToken, iToken, lObjects, dVars):
    if sToken == ':':
        lObjects[iToken] = parser.variable_colon()
        dVars['bVariableColonFound'] = True

def classify_subtype_indication(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':=':
        lObjects[iToken] = parser.variable_subtype_indication(sToken)

def classify_assignment_operator(sToken, iToken, lObjects, dVars):
    if sToken == ':=':
        lObjects[iToken] = parser.variable_assignment_operator()
        dVars['bVariableAssignmentOperatorFound'] = True

def classify_assignment_expression(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ';':
        lObjects[iToken] = parser.variable_assignment_expression(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.variable_semicolon()
        dVars['bVariableKeywordFound'] = False
        dVars['bVariableColonFound'] = False
        dVars['bVariableAssignmentOperatorFound'] = False


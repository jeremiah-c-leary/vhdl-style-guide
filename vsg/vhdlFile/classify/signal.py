import re

from vsg import parser


def signal(self, dVars, lTokens, lObjects, oLine):
    '''
    signal identifier { , identifier } : subtype_indication [ signal kind ] [ := expression ] ;

    NOTE : signal kind is not supported
  
    '''

    if (re.match('^\s*signal\s', oLine.lineLower) or re.match('^\s*signal$', oLine.lineLower)):
        if oLine.insideFunction and not oLine.insideProcedure:
            if not dVars['fFunctionBeginDetected'] and dVars['fFunctionReturnTypeDetected']:
                _assign_beginning_signal_values(oLine, dVars)
        elif oLine.insideProcedure and not oLine.insideFunction:
            if not dVars['fProcedureBeginDetected'] and dVars['fProcedureIsDetected']:
                _assign_beginning_signal_values(oLine, dVars)
        else:
            _assign_beginning_signal_values(oLine, dVars)
            
    if oLine.insideSignal:
        if re.match('.*;', oLine.lineNoComment):
            oLine.isEndSignal = True

    for iToken, sToken in enumerate(lTokens):
        if not dVars['bSignalKeywordFound']:

            classify_signal_keyword(sToken, iToken, lObjects, dVars)

        else:

            if not dVars['bSignalColonFound']:
                classify_colon(sToken, iToken, lObjects, dVars)
                classify_comma(sToken, iToken, lObjects)
                classify_signal_identifier(sToken, iToken, lObjects)
            else:
                if not dVars['bSignalAssignmentOperatorFound']:
                    classify_assignment_operator(sToken, iToken, lObjects, dVars)
                    classify_signal_subtype_indication(sToken, iToken, lObjects)
                else:
                    classify_signal_assignment_expression(sToken, iToken, lObjects)
                classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_signal_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'signal':
        lObjects[iToken] = parser.signal_keyword(sToken)
        dVars['bSignalKeywordFound'] = True 


def classify_signal_identifier(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':' and sToken != ',':
        lObjects[iToken] = parser.signal_identifier(sToken)


def classify_comma(sToken, iToken, lObjects):
    if sToken == ',':
        lObjects[iToken] = parser.signal_comma()


def classify_colon(sToken, iToken, lObjects, dVars):
    if sToken == ':':
        lObjects[iToken] = parser.signal_colon()
        dVars['bSignalColonFound'] = True

def classify_signal_subtype_indication(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ':=':
        lObjects[iToken] = parser.signal_subtype_indication(sToken)

def classify_assignment_operator(sToken, iToken, lObjects, dVars):
    if sToken == ':=':
        lObjects[iToken] = parser.signal_assignment_operator()
        dVars['bSignalAssignmentOperatorFound'] = True

def classify_signal_assignment_expression(sToken, iToken, lObjects):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment) and \
       sToken != ';':
        lObjects[iToken] = parser.signal_assignment_expression(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.signal_semicolon()
        dVars['bSignalKeywordFound'] = False
        dVars['bSignalColonFound'] = False
        dVars['bSignalAssignmentOperatorFound'] = False

def _assign_beginning_signal_values(oLine, dVars):
    oLine.isSignal = True
    oLine.indentLevel = dVars['iCurrentIndentLevel']
    oLine.insideSignal = True


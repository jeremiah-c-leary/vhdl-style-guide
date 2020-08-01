import re

from vsg import parser


def assert_statement(self, dVars, lTokens, lObjects, oLine):
    '''
    [ label : ] assert condition
      [ report expression ]
      [ severity expression ] ;
    '''

    if re.match('^\s*assert', oLine.line, re.IGNORECASE):
        oLine.isAssertKeyword = True
        oLine.insideAssert = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideAssert and not oLine.isAssertKeyword:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    if oLine.insideAssert and ';' in oLine.line:
        oLine.isAssertEnd = True
        dVars['iCurrentIndentLevel'] -= 1

    for iToken, sToken in enumerate(lTokens):

        if not dVars['bAssertKeywordFound']:

            if classify_assert_keyword(sToken, iToken, lObjects, dVars):
                classify_label(self, lObjects)

        else:

            if not dVars['bAssertReportKeywordFound']:
                classify_report_keyword(sToken, iToken, lObjects, dVars)
            else:
                classify_report_expression(sToken, iToken, lObjects, dVars)

            if not dVars['bAssertSeverityKeywordFound']:
                classify_severity_keyword(sToken, iToken, lObjects, dVars)
            else:
                classify_severity_expression(sToken, iToken, lObjects, dVars)

            if not dVars['bAssertReportKeywordFound'] and not dVars['bAssertSeverityKeywordFound']:
                classify_assert_condition(sToken, iToken, lObjects, dVars)

            classify_semicolon(sToken, iToken, lObjects, dVars)


def classify_assert_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'assert':
        lObjects[iToken] = parser.assert_keyword(sToken)
        dVars['bAssertKeywordFound'] = True 
        return True
    return False


def classify_assert_condition(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.assert_condition(sToken)


def classify_report_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'report':
        lObjects[iToken] = parser.assert_report_keyword(sToken)
        dVars['bAssertReportKeywordFound'] = True
        dVars['bAssertSeverityKeywordFound'] = False

def classify_report_expression(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.assert_report_expression(sToken)


def classify_severity_keyword(sToken, iToken, lObjects, dVars):
    if sToken == 'severity':
        lObjects[iToken] = parser.assert_severity_keyword(sToken)
        dVars['bAssertReportKeywordFound'] = False
        dVars['bAssertSeverityKeywordFound'] = True

def classify_severity_expression(sToken, iToken, lObjects, dVars):
    if not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.assert_severity_expression(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.assert_semicolon()
        dVars['bAssertKeywordFound'] = False
        dVars['bAssertReportKeywordFound'] = False
        dVars['bAssertSeverityKeywordFound'] = False

def classify_label(self, lObjects):
    lObjects.reverse()
    bKeywordFound = False
    bLabelColonFound = False
    bLabelFound = False
    for iObject, oObject in enumerate(lObjects):
        if bKeywordFound:
            if type(oObject) == parser.item and bLabelColonFound:
                lObjects[iObject] = parser.assert_label(oObject.get_value())
                bLabelFound = True
                break
            if type(oObject) == parser.item and oObject.get_value() == ':':
                lObjects[iObject] = parser.assert_label_colon()
                bLabelColonFound = True
                
            if isinstance(oObject, parser.semicolon):
                bLabelFound = True
                break
        if type(oObject) == parser.assert_keyword:
            bKeywordFound = True

    lObjects.reverse()

    if not bLabelFound:
        bBreak = False
        for oLine in self.lines[::-1]:
            myObjects = oLine.get_objects()
            myObjects.reverse()
            for iObject, oObject in enumerate(myObjects):
                if type(oObject) == parser.item and bLabelColonFound:
                    myObjects[iObject] = parser.assert_label(oObject.get_value())
                    bBreak = True
                    break
                if type(oObject) == parser.item and oObject.get_value() == ':':
                    myObjects[iObject] = parser.assert_label_colon()
                    bLabelColonFound = True
                if isinstance(oObject, parser.semicolon):
                    bBreak = True
                    break
            myObjects.reverse()
            if bBreak:
                break


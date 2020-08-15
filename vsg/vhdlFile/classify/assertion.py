
from vsg import parser

from vsg.token import assertion as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    assertion ::=
        assert condition
            [ report expression ]
            [ severity expression ]
    '''

    if not dVars['assertion']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['assertion']['report']:

            if classify_report_keyword(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if classify_severity_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_report_expression(oObject, iObject, lObjects, dVars):
                return True 

        if not dVars['assertion']['severity']:

            if classify_report_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_severity_keyword(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if classify_severity_expression(oObject, iObject, lObjects, dVars):
                return True 

        if not dVars['assertion']['report'] and not dVars['assertion']['severity']:

            if classify_condition(oObject, iObject, lObjects, dVars):
                return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'assert':
        lObjects[iObject] = token.keyword(sValue)
        dVars['assertion']['keyword'] = True 
        return True
    return False


def classify_condition(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.condition(oObject.get_value())
        return True
    return False


def classify_report_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'report':
        lObjects[iObject] = token.report_keyword(sValue)
        dVars['assertion']['report'] = True
        dVars['assertion']['severity'] = False
        return True
    return False


def classify_report_expression(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.report_expression(oObject.get_value())
        return True
    return False


def classify_severity_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'severity':
        lObjects[iObject] = token.severity_keyword(sValue)
        dVars['assertion']['report'] = False
        dVars['assertion']['severity'] = True
        return True
    return False


def classify_severity_expression(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.severity_expression(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    dVars['assertion']['keyword'] = False
    dVars['assertion']['report'] = False
    dVars['assertion']['severity'] = False

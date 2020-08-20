
from vsg import parser

from vsg.token import parameter_specification as token

from vsg.vhdlFile.classify import discrete_range


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    parameter_specification ::=
        identifier in discrete_range
    '''

    if not dVars['parameter_specification']['in']:

        if classify_in_keyword(oObject, iObject, lObjects, dVars):
            return True

        if classify_identifier(oObject, iObject, lObjects, dVars):
            return True
    else:

        if discrete_range.tokenize(oObject, iObject, lObjects, dVars):
            return True

    return False


def classify_in_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'in':
        lObjects[iObject] = token.in_keyword(sValue)
        dVars['bEntityKeywordFound'] = True 


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(sValue)
        dVars['bEntityIdentifierFound'] = True


def clear_flags(dVars):
    dVars['parameter_specification']['in'] = False

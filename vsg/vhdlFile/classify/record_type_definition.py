
from vsg import parser
from vsg.token import record_type_definition as token

from vsg.vhdlFile.classify import element_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    record_type_definition ::= 
        record
            element_declaration
            { element_declaration }
        end record [ record_type_simple_name ]
    ''' 
    if not dVars['type_declaration']['record_type_definition']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['type_declaration']['record_type_definition']['end_keyword']:

            if classify_end_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if element_declaration.tokenize(oObject, iObject, lObjects, dVars):
                return True

        else:

            if classify_record_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_simple_name(oObject, iObject, lObjects, dVars):
                return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'record':
        lObjects[iObject] = token.keyword(sValue)
        dVars['type_declaration']['record_type_definition']['keyword'] = True 
        return True
    return False


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['type_declaration']['record_type_definition']['end_keyword'] = True 
        return True
    return False


def classify_record_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'record':
        lObjects[iObject] = token.record_keyword(sValue)
        return True
    return False


def classify_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item and oObject.get_value() != ';':
        lObjects[iObject] = token.simple_name(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['record_type_definition']['keyword'] = False
    dVars['type_declaration']['record_type_definition']['end_keyword'] = False
    element_declaration.clear_flags(dVars)


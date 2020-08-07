
from vsg import parser
from vsg.token import constant_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    constant identifier { , identifier } : subtype_indication [ constant kind ] [ := expression ] ;
  
    '''
    if not dVars['bConstantKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['bConstantColonFound']:

            if classify_colon(oObject, iObject, lObjects, dVars):
                return True

            if classify_comma(oObject, iObject, lObjects):
                return True

            if classify_identifier(oObject, iObject, lObjects):
                return True

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True

            if not dVars['bConstantAssignmentOperatorFound']:

                if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                    return True

                if classify_constant_kind(oObject, iObject, lObjects):
                    return True

                if classify_subtype_indication(oObject, iObject, lObjects):
                    return True

            else:

                if classify_assignment_expression(oObject, iObject, lObjects):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'constant':
        lObjects[iObject] = constant_declaration.keyword(sValue)
        dVars['bConstantKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = constant_declaration.identifier(oObject.get_value())
        return True
    return False


def classify_comma(oObject, iObject, lObjects):
    if oObject.get_value() == ',':
        lObjects[iObject] = constant_declaration.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = constant_declaration.colon()
        dVars['bConstantColonFound'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = constant_declaration.subtype_indication(oObject.get_value())
        return True
    return False


def classify_constant_kind(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        sValue = oObject.get_value()
        if sValue.lower() == 'bus' or sValue.lower() == 'register':
            lObjects[iObject] = constant_declaration.constant_kind(oObject.get_value())
            return True
    return False


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = constant_declaration.assignment_operator()
        dVars['bConstantAssignmentOperatorFound'] = True
        return True
    return False


def classify_assignment_expression(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = constant_declaration.assignment_expression(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = constant_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
        dVars['bConstantKeywordFound'] = False
        dVars['bConstantColonFound'] = False
        dVars['bConstantAssignmentOperatorFound'] = False

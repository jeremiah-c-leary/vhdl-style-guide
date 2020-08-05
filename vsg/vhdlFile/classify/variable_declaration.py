
from vsg import parser
from vsg.token import variable_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    variable identifer_list : subtype_indication [ := expression ]
    '''

    if not dVars['bVariableKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['bVariableColonFound']:

            if classify_colon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_comma(oObject, iObject, lObjects):
                return True 

            if classify_identifier(oObject, iObject, lObjects):
                return True 

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True 

            if not dVars['bVariableAssignmentOperatorFound']:

                if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                    return True 

                if classify_subtype_indication(oObject, iObject, lObjects):
                    return True 

            else:

                if classify_assignment_expression(oObject, iObject, lObjects):
                    return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'variable':
        lObjects[iObject] = variable_declaration.keyword(sValue)
        dVars['bVariableKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = variable_declaration.identifier(oObject.get_value())
        return True
    return False


def classify_comma(oObject, iObject, lObjects):
    if oObject.get_value() == ',':
        lObjects[iObject] = variable_declaration.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = variable_declaration.colon()
        dVars['bVariableColonFound'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = variable_declaration.subtype_indication(oObject.get_value())
        return True
    return False


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = variable_declaration.assignment_operator()
        dVars['bVariableAssignmentOperatorFound'] = True
        return True
    return False


def classify_assignment_expression(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = variable_declaration.assignment_expression(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = variable_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bVariableKeywordFound'] = False
    dVars['bVariableColonFound'] = False
    dVars['bVariableAssignmentOperatorFound'] = False


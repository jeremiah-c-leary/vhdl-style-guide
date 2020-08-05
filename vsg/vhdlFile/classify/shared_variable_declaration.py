
from vsg import parser
from vsg.token import shared_variable_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    shared variable identifer_list : subtype_indication [ := expression ]
    '''

    if not dVars['bSharedVariableKeywordFound']:

        if classify_shared(oObject, iObject, lObjects, dVars):
            return True 

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['bSharedVariableColonFound']:

            if classify_colon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_comma(oObject, iObject, lObjects):
                return True 

            if classify_identifier(oObject, iObject, lObjects):
                return True 

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True 

            if not dVars['bSharedVariableAssignmentOperatorFound']:

                if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                    return True 

                if classify_subtype_indication(oObject, iObject, lObjects):
                    return True 

            else:

                if classify_assignment_expression(oObject, iObject, lObjects):
                    return True 

    return False


def classify_shared(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'shared':
        lObjects[iObject] = shared_variable_declaration.shared_keyword(sValue)
        return True
    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'variable':
        lObjects[iObject] = shared_variable_declaration.variable_keyword(sValue)
        dVars['bSharedVariableKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = shared_variable_declaration.identifier(oObject.get_value())
        return True
    return False


def classify_comma(oObject, iObject, lObjects):
    if oObject.get_value() == ',':
        lObjects[iObject] = shared_variable_declaration.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = shared_variable_declaration.colon()
        dVars['bSharedVariableColonFound'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = shared_variable_declaration.subtype_indication(oObject.get_value())
        return True
    return False


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = shared_variable_declaration.assignment_operator()
        dVars['bSharedVariableAssignmentOperatorFound'] = True
        return True
    return False


def classify_assignment_expression(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = shared_variable_declaration.assignment_expression(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = shared_variable_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bSharedVariableKeywordFound'] = False
    dVars['bSharedVariableColonFound'] = False
    dVars['bSharedVariableAssignmentOperatorFound'] = False


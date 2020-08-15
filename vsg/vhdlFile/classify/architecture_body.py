
from vsg import parser

from vsg.token import architecture_body as token

from vsg.vhdlFile.classify import architecture_declarative_part
from vsg.vhdlFile.classify import architecture_statement_part


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    architecture identifier of *entity*_name is
    
        architecture_declarative_part
    
    begin
    
        architecture_statement_part
    
    end [ architecture ] [ architecture_simple_name ] 
    '''
    if not dVars['architecture_body']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:
        if not dVars['architecture_body']['identifier']:

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True

        else:
            if not dVars['architecture_body']['entity_name']:

                if classify_of_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_entity_name(oObject, iObject, lObjects, dVars):
                    return True

            else:
                if not dVars['architecture_body']['is']:

                    if classify_is_keyword(oObject, iObject, lObjects, dVars):
                        return True
                else:
                    if not dVars['architecture_body']['begin']:

                        if classify_begin_keyword(oObject, iObject, lObjects, dVars):
                            return True

                        if architecture_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                            return True
                    else:
                        if not dVars['architecture_body']['end']:

                            if architecture_statement_part.tokenize(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_end(oObject, iObject, lObjects, dVars):
                                return True

                        else:

                            if classify_end_architecture_keyword(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_semicolon(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_simple_name(oObject, iObject, lObjects, dVars):
                                return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'architecture':
        lObjects[iObject] = token.keyword(sValue)
        dVars['architecture_body']['keyword'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(oObject.get_value())
        dVars['architecture_body']['identifier'] = True
        return True
    return False


def classify_of_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'of':
        lObjects[iObject] = token.of_keyword(sValue)
        return True
    return False


def classify_entity_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.entity_name(oObject.get_value())
        dVars['architecture_body']['entity_name'] = True
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['architecture_body']['is'] = True
        return True
    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['architecture_body']['begin'] = True
        return True
    return False


def classify_end(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['architecture_body']['end'] = True
        return True
    return False


def classify_end_architecture_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'architecture':
        lObjects[iObject] = token.end_architecture_keyword(oObject)
        return True
    return False


def classify_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.simple_name(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['architecture_body']['keyword'] = False
    dVars['architecture_body']['identifier'] = False
    dVars['architecture_body']['entity_name'] = False
    dVars['architecture_body']['is'] = False
    dVars['architecture_body']['begin'] = False
    dVars['architecture_body']['end'] = False


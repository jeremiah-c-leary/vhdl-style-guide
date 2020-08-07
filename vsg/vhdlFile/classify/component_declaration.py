
from vsg import parser
from vsg.token import component_declaration as token

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import port_clause


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    component_declaration ::=
        component identifier [ is ]
            [ local_generic_clause ]
            [ local_port_clause ]
        end component [ component_simple_name ] ;
    '''

    if not dVars['bComponentKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:
        if not dVars['bComponentIdentifierFound']:

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True 

        else:
            if not dVars['bComponentEndKeywordFound']:

                if not dVars['bComponentIsKeywordFound']:
    
                    if classify_is_keyword(oObject, iObject, lObjects, dVars):
                        return True 
    
                if generic_clause.tokenize(oObject, iObject, lObjects, dVars):
                    return True
    
                if port_clause.tokenize(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_keyword(oObject, iObject, lObjects, dVars):
                    return True 

            else:

                if classify_semicolon(oObject, iObject, lObjects, dVars):
                    return True 

                if classify_end_component_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_simple_name(oObject, iObject, lObjects, dVars):
                    return True 

    return False



def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'component':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bComponentKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(sValue)
        dVars['bComponentIdentifierFound'] = True
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['bComponentIsKeywordFound'] = True
        return True
    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['bComponentBeginKeywordFound'] = True
        return True
    return False


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['bComponentEndKeywordFound'] = True 
        return True
    return False


def classify_end_component_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'component':
        lObjects[iObject] = token.end_component_keyword(sValue)
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
    dVars['bComponentKeywordFound'] = False
    dVars['bComponentIdentifierFound'] = False
    dVars['bComponentIsKeywordFound'] = False
    dVars['bComponentEndKeywordFound'] = False


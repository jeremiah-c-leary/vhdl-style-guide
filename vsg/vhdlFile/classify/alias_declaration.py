
from vsg import parser
from vsg.token import alias_declaration as token

from vsg.vhdlFile.classify import alias_designator


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    alias_declaration ::=
        alias alias_designator [ : subtype_indication ] is name [ signature ] ;
    ''' 

    if not dVars['alias_declaration']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['alias_declaration']['aliasDesignator']:

            if alias_designator.tokenize(oObject, iObject, lObjects, dVars):
                dVars['alias_declaration']['aliasDesignator'] = True
                return True

        else:
            if not dVars['alias_declaration']['colon'] and not dVars['alias_declaration']['isKeyword']:

                if classify_colon(oObject, iObject, lObjects, dVars):
                    return True 

            if not dVars['alias_declaration']['isKeyword']:

                if classify_is_keyword(oObject, iObject, lObjects, dVars):
                    return True 

            else:

                if not dVars['alias_declaration']['name']:

                    if classify_name(oObject, iObject, lObjects, dVars):
                        return True 

                else:
                    
                    if classify_semicolon(oObject, iObject, lObjects, dVars):
                        return True 


                    if classify_signature(oObject, iObject, lObjects, dVars):
                        return True 

            if dVars['alias_declaration']['colon'] and not dVars['alias_declaration']['isKeyword']:

                if classify_subtype_indication(oObject, iObject, lObjects, dVars):
                    return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'alias':
        lObjects[iObject] = token.keyword(sValue)
        dVars['alias_declaration']['keyword'] = True 
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = token.colon()
        dVars['alias_declaration']['colon'] = True
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['alias_declaration']['isKeyword'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.subtype_indication(oObject.get_value())
        return True
    return False


def classify_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.name(oObject.get_value())
        dVars['alias_declaration']['name'] = True
        return True
    return False


def classify_signature(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.signature(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
        dVars['alias_declaration']['keyword'] = False
        dVars['alias_declaration']['aliasDesignator'] = False
        dVars['alias_declaration']['colon'] = False
        dVars['alias_declaration']['isKeyword'] = False
        dVars['alias_declaration']['name'] = False

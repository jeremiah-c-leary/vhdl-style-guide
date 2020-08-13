
from vsg import parser
from vsg.token import entity as token

from vsg.vhdlFile.classify import entity_header


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    entity_declaration ::=
        entity identifier is
            [ entity_header ]
            [ entity_declarative_part ]
        [ begin
            entity_statement_part ]
        end [ entity ] [ entity_simple_name ] ;

    '''

    if not dVars['bEntityKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:
        if not dVars['bEntityIdentifierFound']:

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True 

        else:
            if not dVars['bEntityIsKeywordFound']:

                if classify_is_keyword(oObject, iObject, lObjects, dVars):
                    return True 

            else:

                if not dVars['bEntityBeginKeywordFound']:

                    if entity_header.tokenize(oObject, iObject, lObjects, dVars):
                        return True 

                    if classify_begin_keyword(oObject, iObject, lObjects, dVars):
                        return True 


                if not dVars['bEntityEndKeywordFound']:

                    if classify_end_keyword(oObject, iObject, lObjects, dVars):
                        return True 

                else:
                    if classify_end_entity_keyword(oObject, iObject, lObjects, dVars):
                        return True

                    if classify_simple_name(oObject, iObject, lObjects, dVars):
                        return True 

                    if classify_semicolon(oObject, iObject, lObjects, dVars):
                        return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'entity':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bEntityKeywordFound'] = True 


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(sValue)
        dVars['bEntityIdentifierFound'] = True


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['bEntityIsKeywordFound'] = True


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['bEntityBeginKeywordFound'] = True


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['bEntityEndKeywordFound'] = True 


def classify_end_entity_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'entity':
        lObjects[iObject] = token.end_entity_keyword(sValue)
        return True
    return False


def classify_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.simple_name(oObject.get_value())


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)

def clear_flags(dVars):
    entity_header.clear_flags(dVars)
    dVars['bEntityKeywordFound'] = False
    dVars['bEntityIdentifierFound'] = False
    dVars['bEntityIsKeywordFound'] = False
    dVars['bEntityBeginKeywordFound'] = False
    dVars['bEntityEndKeywordFound'] = False


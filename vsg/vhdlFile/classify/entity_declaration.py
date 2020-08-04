
from vsg import parser
from vsg.token import entity as token

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import port_clause


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
        classify_keyword(oObject, iObject, lObjects, dVars)
    else:
        if not dVars['bEntityIdentifierFound']:
            classify_identifier(oObject, iObject, lObjects, dVars)
        else:
            if not dVars['bEntityIsKeywordFound']:
                classify_is_keyword(oObject, iObject, lObjects, dVars)
            else:

                if not dVars['bEntityBeginKeywordFound']:
                    entity_header(oObject, iObject, lObjects, dVars)
                    classify_begin_keyword(oObject, iObject, lObjects, dVars)

                if not dVars['bEntityEndKeywordFound']:
                    classify_end_keyword(oObject, iObject, lObjects, dVars)
                else:
                    if classify_end_entity_keyword(oObject, iObject, lObjects, dVars):
                        return
                    classify_simple_name(oObject, iObject, lObjects, dVars)
                    classify_semicolon(oObject, iObject, lObjects, dVars)


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


def entity_header(oObject, iObject, lObjects, dVars):
    '''
    entity_header ::=
        [ formal_generic_clause ]
        [ formal_port_clause ]
    '''
    if not dVars['bPortClauseKeywordFound']:
        generic_clause.tokenize(oObject, iObject, lObjects, dVars)
    if not dVars['bGenericClauseKeywordFound']:
        port_clause.tokenize(oObject, iObject, lObjects, dVars)


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
        dVars['bEntityKeywordFound'] = False
        dVars['bEntityIdentifierFound'] = False
        dVars['bEntityIsKeywordFound'] = False
        dVars['bEntityBeginKeywordFound'] = False
        dVars['bEntityEndKeywordFound'] = False

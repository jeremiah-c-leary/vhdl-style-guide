
from vsg.vhdlFile import utils

from vsg.token import entity_declaration as token


'''
entity_declaration ::=
    entity identifier is
        entity_header
        entity_declarative_part
    [ begin
        entity_statement_part ]
    end [ entity ] [ entity_simple_name ] ;
'''

def check_for(oObject, lNewObjects, dVars):
    if oObject.get_value().lower() == 'entity':
        return True
    return False


def classify_begin_declaration(oObject, lNewObjects, dVars):
    '''
    entity identifier is
    '''
    if entity_keyword(oObject, lNewObjects):
        return True
    elif is_keyword(oObject, lNewObjects):
        utils.pop_level(dVars)
        utils.push_level(dVars, 'entity_header')
        return True
    else:
        lNewObjects.append(token.identifier(oObject.get_value()))
        return True
    return False


def classify_end_declaration(oObject, lNewObjects, dVars):
    '''
    end [ entity ] [ entity_simple_name ] ;
    '''
    if end_keyword(oObject, lNewObjects):
        return True
    elif end_entity_keyword(oObject, lNewObjects):
        return True
    elif semicolon(oObject, lNewObjects):
        utils.pop_level(dVars)
        return True
    else:
        lNewObjects.append(token.entity_simple_name(oObject.get_value()))
        return True
    return False


def entity_keyword(oObject, lNewObjects):
    return utils.is_object('entity', token.entity_keyword, oObject, lNewObjects)


def is_keyword(oObject, lNewObjects):
    return utils.is_object('is', token.is_keyword, oObject, lNewObjects)


def end_keyword(oObject, lNewObjects):
    return utils.is_object('end', token.end_keyword, oObject, lNewObjects)


def end_entity_keyword(oObject, lNewObjects):
    return utils.is_object('entity', token.end_entity_keyword, oObject, lNewObjects)


def semicolon(oObject, lNewObjects):
    return utils.is_object(';', token.semicolon, oObject, lNewObjects)


from vsg.vhdlFile import utils

from vsg.token import architecture_body as token

'''
architecture identifier of *entity*_name is
    architecture_declarative_part
begin
    architecture_statement_part
end [ architecture ] [ architecture_simple_name ] ;
'''

def check_for(oObject, lNewObjects, dVars):
    if oObject.get_value().lower() == 'architecture':
        return True
    return False


def classify_begin_declaration(oObject, lNewObjects, dVars):
    '''
    architecture identifier of *entity*_name is
    '''
    if is_keyword(oObject, lNewObjects):
        utils.push_level(dVars, 'architecture_declarative_part')
        return True
    elif of_keyword(oObject, lNewObjects):
        dVars['blue'] = True
        return True
    elif architecture_keyword(oObject, lNewObjects):
        return True
    elif not dVars['blue']:
        lNewObjects.append(token.identifier(oObject.get_value()))
        return True
    else:
        lNewObjects.append(token.entity_name(oObject.get_value()))
        dVars['blue'] = False
        return True

    return False


def classify_end_declaration(oObject, lNewObjects, dVars):
    '''
    end [ architecture ] [ architecture_simple_name ] ;
    '''
    if end_keyword(oObject, lNewObjects):
        return True
    elif end_architecture_keyword(oObject, lNewObjects):
        return True
    elif semicolon(oObject, lNewObjects):
        utils.pop_level(dVars)
        return True
    else:
        lNewObjects.append(token.architecture_simple_name(oObject.get_value()))
        return True

    return False


def end_keyword(oObject, lNewObjects):
    return utils.is_object('end', token.end_keyword, oObject, lNewObjects)


def architecture_keyword(oObject, lNewObjects):
    return utils.is_object('architecture', token.architecture_keyword, oObject, lNewObjects)


def is_keyword(oObject, lNewObjects):
    return utils.is_object('is', token.is_keyword, oObject, lNewObjects)


def of_keyword(oObject, lNewObjects):
    return utils.is_object('of', token.of_keyword, oObject, lNewObjects)


def end_architecture_keyword(oObject, lNewObjects):
    return utils.is_object('architecture', token.end_architecture_keyword, oObject, lNewObjects)


def semicolon(oObject, lNewObjects):
    return utils.is_object(';', token.semicolon, oObject, lNewObjects)



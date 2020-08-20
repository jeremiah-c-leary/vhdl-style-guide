
from vsg.vhdlFile import utils

from vsg.token import architecture_body as token

def classify(oObject, lNewObjects, dVars):
    '''
    architecture identifier of *entity*_name is
        architecture_declarative_part
    begin
        architecture_statement_part
    end [ architecture ] [ architecture_simple_name ] 
    '''
    if is_keyword(oObject, lNewObjects):
        utils.push_level(dVars, 'architecture_declarative_part')
        return True
    elif of_keyword(oObject, lNewObjects):
        return True
    elif end_architecture_keyword(oObject, lNewObjects):
        return True
    elif semicolon(oObject, lNewObjects):
        utils.pop_level(dVars)
        return True

    return False


def is_keyword(oObject, lNewObjects):
    return utils.is_object('is', token.is_keyword, oObject, lNewObjects)


def of_keyword(oObject, lNewObjects):
    return utils.is_object('of', token.of_keyword, oObject, lNewObjects)


def end_architecture_keyword(oObject, lNewObjects):
    return utils.is_object('architecture', token.end_architecture_keyword, oObject, lNewObjects)


def semicolon(oObject, lNewObjects):
    return utils.is_object(';', token.semicolon, oObject, lNewObjects)



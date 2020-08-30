
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import if_generate_statement as token

from vsg.vhdlFile.classify import parameter_specification
from vsg.vhdlFile.classify import generate_statement_body


def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    print('--> if_generate_statement.is_it')
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == 'if':
                utils.push_level(dVars, 'if_generate_statement:end_declaration')
                utils.push_level(dVars, 'if_generate_statement:begin_declaration')
                lNewObjects.append(token.label_name(oObject.get_value()))
                return True

        if oObject.get_value().lower() == 'elsif':
                utils.pop_level(dVars)
                utils.push_level(dVars, 'if_generate_statement:elsif_declaration')
                lNewObjects.append(token.elsif_keyword(oObject.get_value()))
                return True

        if oObject.get_value().lower() == 'else':
                utils.pop_level(dVars)
                utils.push_level(dVars, 'if_generate_statement:else_declaration')
                lNewObjects.append(token.else_keyword(oObject.get_value()))
                return True

    except IndexError:
        return False
    return False


def tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):

#    print('--> if_generate_statement.tokenize_begin_declaration')
    if oObject.get_value().lower() == ':':
        lNewObjects.append(token.label_colon())
        return True
    elif oObject.get_value().lower() == 'if':
        lNewObjects.append(token.if_keyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.generate_keyword(oObject.get_value()))
        utils.pop_level(dVars)
        utils.push_level(dVars, 'generate_statement_body')
        return True
    else:
        lNewObjects.append(token.condition(oObject.get_value()))
        return True

    return False


def tokenize_elsif_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    print('--> if_generate_statement.tokenize_elsif_declaration')
#    if oObject.get_value().lower() == 'elsif':
#        lNewObjects.append(token.elsif_keyword(oObject.get_value()))
    if oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.generate_keyword(oObject.get_value()))
        utils.pop_level(dVars)
        utils.push_level(dVars, 'generate_statement_body')
        return True
    else:
        lNewObjects.append(token.condition(oObject.get_value()))
        return True
    return False


def tokenize_else_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    if oObject.get_value().lower() == 'else':
#        lNewObjects.append(token.else_keyword(oObject.get_value()))
#    print('--> if_generate_statement.tokenize_else_declaration')
    if oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.generate_keyword(oObject.get_value()))
        utils.pop_level(dVars)
        utils.push_level(dVars, 'generate_statement_body')
        return True

    return False


def tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    print('--> if_generate_statement.tokenize_end_declaration')
    if oObject.get_value().lower() == 'end':
        lNewObjects.append(token.end_keyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.end_generate_keyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == ';':
        lNewObjects.append(token.semicolon())
        utils.pop_level(dVars)
        return True

    return False

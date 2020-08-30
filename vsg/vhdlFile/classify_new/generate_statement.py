
from vsg.vhdlFile.classify_new import for_generate_statement
from vsg.vhdlFile.classify_new import if_generate_statement
from vsg.vhdlFile.classify_new import case_generate_statement
from vsg.vhdlFile import utils

from vsg import token
from vsg.token import if_generate_statement as igs_token


def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
    '''
    generate_statement ::=
        for_generate_statement
      | if_generate_statement
      | case_generate_statement
    '''
#    print('--> generate_statement.is_it')
    if for_generate_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
        utils.push_level(dVars, 'for_generate_statement:begin_declaration')
        lNewObjects.append(token.for_generate_statement.label_name(oObject.get_value()))
        return True

    if if_generate_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True

    if case_generate_statement.is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
        return True

    return False


def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    print('--> generate_statement.tokenize')
    if utils.is_current_level(dVars, 'for_generate_statement:begin_declaration'):
        return for_generate_statement.tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars)
    if utils.is_current_level(dVars, 'for_generate_statement:end_declaration'):
        return for_generate_statement.tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars)

    if utils.is_current_level(dVars, 'if_generate_statement:begin_declaration'):
        if if_generate_statement.tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True
    elif utils.is_current_level(dVars, 'if_generate_statement:elsif_declaration'):
        if if_generate_statement.tokenize_elsif_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True
    elif utils.is_current_level(dVars, 'if_generate_statement:else_declaration'):
        if if_generate_statement.tokenize_else_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True
    elif utils.is_current_level(dVars, 'if_generate_statement:end_declaration'):
        if if_generate_statement.tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True

    if utils.is_current_level(dVars, 'case_generate_statement:begin_declaration'):
        if case_generate_statement.tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True
    elif utils.is_current_level(dVars, 'case_generate_statement:end_declaration'):
        if case_generate_statement.tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
            return True
    return False

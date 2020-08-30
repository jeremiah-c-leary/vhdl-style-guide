
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import case_generate_alternative as token

'''
case_generate_alternative ::= [§ 11.8]
    when [ *alternative*_label : ] choices =>
        generate_statement_body
'''


def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if oObject.get_value().lower() == 'when':
        lNewObjects.append(token.WhenKeyword(oObject.get_value()))
        utils.push_level(dVars, 'generate_statement_body')
        utils.push_level(dVars, 'case_generate_alternative:declaration')
        return True
    return False


def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):

    if oObject.get_value().lower() == '=>':
        lNewObjects.append(token.Assignment(oObject.get_value()))
        utils.pop_level(dVars)
        return True
    else:
        lNewObjects.append(oObject)
        return True

    return False

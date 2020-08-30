
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import block_statement as token

from vsg.vhdlFile.classify import block_header
from vsg.vhdlFile.classify import block_declarative_part
from vsg.vhdlFile.classify import block_statement_part

def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == 'block':
                lNewObjects.append(token.label_name(oObject.get_value()))
                utils.push_level(dVars, 'block_statement:end_declaration')
                utils.push_level(dVars, 'block_statement:begin_declaration')
                return True
    except IndexError:
        return False
    return False


def tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):

    if oObject.get_value().lower() == ':':
        lNewObjects.append(token.label_colon())
        return True
    elif oObject.get_value().lower() == 'block':
       lNewObjects.append(token.keyword(oObject.get_value()))
       return True
    elif utils.have_guard_condition(iObject, lAllObjects):
       print("need to process guard condition first")
       return True
    elif utils.have_is_keyword(iObject, lAllObjects):
       lNewObjects.append(token.is_keyword(oObject.get_value()))
       return True
    elif oObject.get_value().lower() == 'begin':
       lNewObjects.append(token.begin_keyword(oObject.get_value()))
       utils.pop_level(dVars)
       utils.push_level(dVars, 'block_statement_part')
       return True

    return False

def tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if oObject.get_value().lower() == 'block':
        lNewObjects.append(token.end_block_keyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == ';':
        lNewObjects.append(token.semicolon())
        utils.pop_level(dVars)
        return True
    else:
        lNewObjects.append(token.end_block_label(oObject.get_value()))
        return True

    return False


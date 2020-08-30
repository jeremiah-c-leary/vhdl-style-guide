
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import case_generate_statement as token

'''
case_generate_statement ::=
    *generate*_label :
        case expression generate
            case_generate_alternative
            { case_generate_alternative }
        end generate [ *generate*_label ] ;
'''


def is_it(iObject, oObject, lAllObjects, lNewObjects, dVars):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lAllObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lAllObjects[iIndex-1].get_value().lower() == 'case':
                lNewObjects.append(token.LabelName(oObject.get_value()))
                utils.push_level(dVars, 'case_generate_statement:end_declaration')
                utils.push_level(dVars, 'case_generate_alternative')
                utils.push_level(dVars, 'case_generate_statement:begin_declaration')
                return True
    except IndexError:
        return False
    return False


def tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):

    if oObject.get_value().lower() == ':':
        lNewObjects.append(token.LabelColon())
        return True
    elif oObject.get_value().lower() == 'case':
        lNewObjects.append(token.CaseKeyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.GenerateKeyword(oObject.get_value()))
        utils.pop_level(dVars)
        return True

    return False


def tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
    if oObject.get_value().lower() == 'end':
        lNewObjects.append(token.EndKeyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == 'generate':
        lNewObjects.append(token.EndGenerateKeyword(oObject.get_value()))
        return True
    elif oObject.get_value().lower() == ';':
        lNewObjects.append(token.Semicolon())
        utils.pop_level(dVars)
        return True
    else:
        lNewObjects.append(token.EndGenerateLabel(oObject.get_value()))
        return True

    return False

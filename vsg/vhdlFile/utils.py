
from vsg import token
from vsg import parser


def is_object(sType, oType, oObject, lNewObjects):
    if oObject.get_value().lower() == sType:
        lNewObjects.append(oType(oObject.get_value()))
        return True
    return False


def is_current_level(dVars, sLevel):
    if current_level(dVars) == sLevel:
        return True
    return False

def pop_level(dVars):
    dVars['history'].pop()

def push_level(dVars, level):
    dVars['history'].append(level)

def current_level(dVars):
    return dVars['history'][-1]


def is_comment(oObject, lNewObjects):
    if type(oObject) == token.Comment:
        return True
    return False


def is_carriage_return(oObject, lNewObjects):
    if type(oObject) == token.CarriageReturn:
        return True
    return False


def is_blank_line(oObject, lNewObjects):
    if type(oObject) == token.BlankLine:
        return True
    return False


def is_whitespace(oObject, lNewObjects):
    if type(oObject) == token.Whitespace:
        return True
    return False

def have_guard_condition(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == '(':
                return True
        iIndex += 1
    return False

def have_is_keyword(iObject, lAllObjects):
    iItemCount = 0
    iIndex = iObject
    while iItemCount < 1:
        if type(lAllObjects[iIndex]) == parser.item:
            iItemCount += 1
            if lAllObjects[iIndex].get_value().lower() == 'is':
                return True
        iIndex += 1
    return False


from vsg import parser

from vsg.token import block_statement as token

from vsg.vhdlFile.classify import block_header
from vsg.vhdlFile.classify import block_declarative_part
from vsg.vhdlFile.classify import block_statement_part


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    block_statement ::=
        block_label :
            block [ ( *guard*_condition ) ] [ is ]
                block_header
                block_declarative_part
            begin
                block_statement_part
            end block [ *block*_label ] ;
    '''
    dVars['caller'] = 'block_statement'
    if not dVars['block_statement']['end']:
        if not dVars['block_statement']['keyword']:
    
    
            if classify_keyword(oObject, iObject, lObjects, dVars):
                return True
    
        else:
    
            if not dVars['block_statement']['is']:
    
                if classify_is_keyword(oObject, iObject, lObjects, dVars):
                    return True
    
                if classify_guard_condition(oObject, iObject, lObjects, dVars):
                    return True
    
            else:
    
                if not dVars['block_statement']['begin']:
    
                    if classify_begin_keyword(oObject, iObject, lObjects, dVars):
                        return True
    
                    if block_header.tokenize(oObject, iObject, lObjects, dVars):
                        return True
    
                    if block_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                        return True

    if len(dVars['history']) > 0 and dVars['history'][-1] == 'begin':
        
        if not dVars['block_statement']['end']:
#            if block_statement_part.tokenize(oObject, iObject, lObjects, dVars):
#                return True

            if classify_end_keyword(oObject, iObject, lObjects, dVars):
                return True

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True

            if classify_end_block_keyword(oObject, iObject, lObjects, dVars):
                return True

            if classify_end_block_label(oObject, iObject, lObjects, dVars):
                return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'block':
        lObjects[iObject] = token.keyword(sValue)
        dVars['block_statement']['keyword'] = True 
        return True
    return False


def classify_guard_condition(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.guard_condition(oObject.get_value())
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['block_statement']['is'] = True
        return True
    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['block_statement']['begin'] = True
        dVars['history'].append('begin')
        clear_flags(dVars)
        return True
    return False


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['block_statement']['end'] = True
        return True
    return False


def classify_end_block_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'block':
        lObjects[iObject] = token.end_block_keyword(sValue)
        return True
    return False


def classify_end_block_label(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.end_block_label(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        dVars['history'].pop()
        clear_flags(dVars)
        dVars['block_statement']['end'] = False
        return True
    return False


def clear_flags(dVars):
    dVars['block_statement']['keyword'] = False
    dVars['block_statement']['is'] = False
    dVars['block_statement']['begin'] = False


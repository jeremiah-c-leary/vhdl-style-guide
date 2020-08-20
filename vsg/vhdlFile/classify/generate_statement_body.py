
from vsg.vhdlFile.classify import block_declarative_part
from vsg.vhdlFile.classify import concurrent_statement


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    generate_statement_body ::=
            [ block_declarative_part
        begin ]
            { concurrent_statement }
        [ end [ alternative_label ] ; ]
    '''
    if not dVars['generate_statement_body']['begin'] and not dVars['generate_statement_body']['no_begin']:

        if block_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
            return True

        if classify_begin_keyword(oObject, iObject, lObjects, dVars):
            return True

    if len(dVars['history']) > 0 and dVars['history'][-1] == 'for_generate':

#       if concurrent_statement.tokenize(oObject, iObject, lObjects, dVars):
#           dVars['generate_statement_body']['no_begin'] = True
#           return True

        if dVars['generate_statement_body']['begin']:
    
            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True
    
            if classify_end_keyword(oObject, iObject, lObjects, dVars):
                return True
    
            if classify_end_alternate_label(oObject, iObject, lObjects, dVars):
                return True

    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['generate_statement_body']['begin'] = True
        return True
    return False


def classify_end_alternative_label(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.end_alternative_label(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['generate_statement_body']['begin'] = False
    dVars['generate_statement_body']['no_begin'] = False


from vsg import parser
from vsg.token import process_statement as token

from vsg.vhdlFile.classify import process_declarative_part
from vsg.vhdlFile.classify import process_sensitivity_list
from vsg.vhdlFile.classify import process_statement_part

iOpenParenthesis = 0
iCloseParenthesis = 0


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    process_statement ::=
        [ process_label : ]
            [ postponed ] process [ ( process_sensitivity_list ) ] [ is ]
                process_declarative_part
            begin
                process_statement_part
            end [ postponed ] process [ process_label ] ;
    '''
    if not dVars['process_statement']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['process_statement']['begin']:

            if classify_is_keyword(oObject, iObject, lObjects, dVars):
                return True

            if classify_begin_keyword(oObject, iObject, lObjects, dVars):
                return True

            if process_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                return True

            if not dVars['process_statement']['open_parenthesis']:

                if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
   
            else:

                if not dVars['process_statement']['close_parenthesis']: 

                    update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis)
    
                    if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                        return True

                    if process_sensitivity_list.tokenize(oObject, iObject, lObjects, dVars):
                        return True

        else:

            if not dVars['process_statement']['end']:

                if process_statement_part.tokenize(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_keyword(oObject, iObject, lObjects, dVars):
                    return True

            else:

                if classify_semicolon(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_postponed_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_process_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_end_process_label_name(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'process':
        lObjects[iObject] = token.keyword(sValue)
        dVars['process_statement']['keyword'] = True
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        iOpenParenthesis = 1
        iCloseParenthesis = 0
        dVars['process_statement']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        if iOpenParenthesis == iCloseParenthesis:
            lObjects[iObject] = token.close_parenthesis()
            dVars['process_statement']['close_parenthesis'] = True
            return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        return True
    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = token.begin_keyword(sValue)
        dVars['process_statement']['begin'] = True
        return True
    return False


def classify_end_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = token.end_keyword(sValue)
        dVars['process_statement']['end'] = True
        return True
    return False


def classify_end_postponed_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'postponed':
        lObjects[iObject] = token.end_postponed_keyword(oObject)
        return True
    return False


def classify_end_process_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'process':
        lObjects[iObject] = token.end_process_keyword(oObject)
        return True
    return False


def classify_end_process_label_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.end_process_label_name(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['process_statement']['keyword'] = False
    dVars['process_statement']['open_parenthesis'] = False
    dVars['process_statement']['close_parenthesis'] = False
    dVars['process_statement']['begin'] = False
    dVars['process_statement']['end'] = False


def update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis):
    if oObject.get_value() == '(':
        iOpenParenthesis += 1
    if oObject.get_value() == ')':
        iCloseParenthesis += 1

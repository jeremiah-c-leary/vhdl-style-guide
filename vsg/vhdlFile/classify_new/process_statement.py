
from vsg.token import process_statement as token

from vsg.vhdlFile.classify_new import process_declarative_part
from vsg.vhdlFile.classify_new import process_statement_part
from vsg.vhdlFile.classify_new import process_sensitivity_list

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    process_statement ::=
        [ *process*_label : ]
            [ postponed ] process [ ( process_sensitivity_list ) ] [ is ]
                process_declarative_part
            begin
                process_statement_part
            end [ postponed ] process [ *process*_label ] ;
    '''
    if utils.find_in_next_n_tokens('process', 4, iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iCurrent, lObjects):
    iToken = iCurrent

    classify_opening_declaration(iToken, lObjects)

    process_declarative_part.detect(iToken, lObjects)

    iLast = 0
    while iLast != iToken:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.object_value_is(lObjects, iToken, 'begin'):
            utils.assign_token(lObjects, iToken, token.begin_keyword)
            iToken += 1
            break
    
        process_statement_part.detect(iToken, lObjects)

    iLast = 0
    while iLast != iToken:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.object_value_is(lObjects, iToken, 'end'):
            break
    
        process_statement_part.detect(iToken, lObjects)

    classify_closing_declaration(iToken, lObjects)

    return iToken


def classify_opening_declaration(iToken, lObjects):
    iCurrent = utils.find_next_token(iToken, lObjects)
    iCurrent = utils.tokenize_label(iCurrent, lObjects, token.process_label, token.label_colon)
    iCurrent = utils.assign_next_token_if('postponed', token.postponed_keyword, iCurrent, lObjects) 
    iCurrent = utils.assign_next_token_required('process', token.process_keyword, iCurrent, lObjects)

    if utils.is_next_token('(', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = process_sensitivity_list.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iCurrent, lObjects) 
    return iCurrent

        
def classify_closing_declaration(iToken, lObjects):
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('process', token.end_process_keyword, iToken, lObjects):
            continue
        if utils.classify_token('postponed', token.end_postponed_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_process_label)

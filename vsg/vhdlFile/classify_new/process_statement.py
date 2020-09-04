
from vsg.token import process_statement as token

from vsg.vhdlFile.classify_new import process_declarative_part
from vsg.vhdlFile.classify_new import process_statement_part
from vsg.vhdlFile.classify_new import process_sensitivity_list

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    process_statement ::=
        [ *process*_label : ]
            [ postponed ] process [ ( process_sensitivity_list ) ] [ is ]
                process_declarative_part
            begin
                process_statement_part
            end [ postponed ] process [ *process*_label ] ;
    '''
    iToken = iCurrent
    iTokenCount = 0
    while iTokenCount < 5:
        iToken = utils.find_next_token(iToken, lObjects)
        iTokenCount += 1
        if utils.object_value_is(lObjects, iToken, 'process'):
            return classify(iCurrent, lObjects)
        iToken += 1
    return iCurrent


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
    iToken = utils.find_next_token(iToken, lObjects)
    iToken = utils.tokenize_label(iToken, lObjects, token.process_label, token.label_colon)
    iToken = utils.find_next_token(iToken, lObjects)
    iToken = utils.tokenize_postponed(iToken, lObjects, token.postponed_keyword)

    iToken = utils.find_next_token(iToken, lObjects)
    utils.assign_token(lObjects, iToken, token.process_keyword)
    iToken += 1

    iToken = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iToken, '('):
        utils.assign_token(lObjects, iToken, token.open_parenthesis)
        iToken = utils.find_next_token(iToken, lObjects)
        process_sensitivity_list.classify(iToken, lObjects)
        iToken = utils.find_next_token(iToken, lObjects)
        utils.assign_token(lObjects, iToken, token.close_parenthesis)

    iToken = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iToken, 'is'):
        utils.assign_token(lObjects, iToken, token.is_keyword)
        iToken += 1

        
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

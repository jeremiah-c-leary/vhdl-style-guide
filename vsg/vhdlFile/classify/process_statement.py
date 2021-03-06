
from vsg.token import process_statement as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import process_declarative_part
from vsg.vhdlFile.classify import process_statement_part
from vsg.vhdlFile.classify import process_sensitivity_list


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
        if not utils.find_in_next_n_tokens(';', 3, iToken, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = process_declarative_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = process_statement_part.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.process_label, token.label_colon)
    iCurrent = utils.assign_next_token_if('postponed', token.postponed_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('process', token.process_keyword, iCurrent, lObjects)

    if utils.is_next_token('(', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
        iCurrent = process_sensitivity_list.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('postponed', token.end_postponed_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('process', token.end_process_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_process_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

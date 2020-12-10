
from vsg.vhdlFile import utils

from vsg.token import block_statement as token

from vsg.vhdlFile.classify import block_declarative_part
from vsg.vhdlFile.classify import block_header
from vsg.vhdlFile.classify import block_statement_part


def detect(iToken, lObjects):
    '''
    block_statement ::=
    block_label :
        block [ ( *guard*_condition ) ] [ is ]
            block_header
            block_declarative_part
        begin
            block_statement_part
        end block [ block_label ] ;
    '''

    if utils.are_next_consecutive_tokens([None, ':', 'block'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.tokenize_label(iToken, lObjects, token.block_label, token.label_colon)
    iCurrent = utils.assign_next_token_required('block', token.block_keyword, iCurrent, lObjects)

    if utils.is_next_token('(', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('(', token.guard_open_parenthesis, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if_not(')', token.guard_condition, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(')', token.guard_close_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = block_header.detect(iCurrent, lObjects)

    iCurrent = block_declarative_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = block_statement_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('block', token.end_block_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_block_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

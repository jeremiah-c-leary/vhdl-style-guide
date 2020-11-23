
from vsg.token import generate_statement_body as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import block_declarative_part
from vsg.vhdlFile.classify import concurrent_statement


def classify(iToken, lObjects):
    '''
    generate_statement_body ::=
            [ block_declarative_part
        begin ]
            { concurrent_statement }
        [ end [ alternative_label ] ; ]
    '''
    iCurrent = utils.find_next_token(iToken, lObjects)
    iLast = iCurrent
    iCurrent = block_declarative_part.detect(iCurrent, lObjects)

    if iCurrent != iLast:
        iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if('begin', token.begin_keyword, iCurrent, lObjects)

    iLast = 0
    while iCurrent != iLast:
        iLast = iCurrent
        if utils.is_next_token_one_of(['elsif', 'else', 'when'], iCurrent, lObjects):
            return iCurrent
        if utils.is_next_token_one_of(['end'], iCurrent, lObjects):
            break
        iCurrent = concurrent_statement.detect(iCurrent, lObjects)

    if not utils.are_next_consecutive_tokens(['end', 'generate'], iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if_not(';', token.alternative_label, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

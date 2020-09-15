
from vsg.token import generate_statement_body as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import block_declarative_part
from vsg.vhdlFile.classify_new import concurrent_statement


def classify(iToken, lObjects):
    '''
    generate_statement_body ::=
            [ block_declarative_part
        begin ]
            { concurrent_statement }
        [ end [ alternative_label ] ; ]
    '''

    bBlockDeclarativePartFound = False
    iCurrent = utils.find_next_token(iToken, lObjects)
    iLast = iCurrent
    iCurrent = block_declarative_part.detect(iCurrent, lObjects)

    if iCurrent != iLast:
        bBlockDeclarativePartFound = True
        iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iLast = 0
    while iCurrent != iLast:
        iLast = iCurrent
        if utils.is_next_token_one_of(['elsif', 'else', 'when', 'end'], iCurrent, lObjects):
            return iCurrent
        iCurrent = concurrent_statement.detect(iCurrent, lObjects)

    if bBlockDeclarativePartFound:
        iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_if_not(';', token.alternative_label, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent


from vsg.token import block_configuration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import block_specification
from vsg.vhdlFile.classify import use_clause
from vsg.vhdlFile.classify import configuration_item


def detect(iToken, lObjects):
    '''
    block_configuration ::=
        for block_specification
            { use_clause }
            { configuration_item }
        end for ;
    '''

    if utils.is_next_token('for', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('for', token.for_keyword, iToken, lObjects)

    iCurrent = block_specification.classify(iCurrent, lObjects)

    iStop = len(lObjects)
    while iCurrent < iStop:
        iPrevious = iCurrent
        iCurrent = use_clause.detect(iCurrent, lObjects)
        if iPrevious == iCurrent:
            break
    

    while iCurrent < iStop:
        iPrevious = iCurrent
        iCurrent = configuration_item.classify(iCurrent, lObjects)
        if iPrevious == iCurrent:
            break

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('for', token.end_for_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

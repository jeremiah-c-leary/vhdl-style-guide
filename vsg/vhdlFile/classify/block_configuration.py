
from vsg.token import block_configuration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import utils as c_utils

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

    iCurrent = c_utils.classify_production(use_clause, iCurrent, lObjects)
    iCurrent = c_utils.classify_production(configuration_item, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('for', token.end_for_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.unspecified, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

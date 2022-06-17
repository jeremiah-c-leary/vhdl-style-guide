
from vsg.token import unbounded_array_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import index_subtype_definition
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    unbounded_array_definition ::=
        array ( index_subtype_definition { , index_subtype_definition } )
            of *element*_subtype_indication
    '''

    if utils.is_next_token('array', iToken, lObjects):
        if utils.find_in_next_n_tokens('<>', 5, iToken, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('array', token.array_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('(', token.open_parenthesis, iCurrent, lObjects)
    iCurrent = index_subtype_definition.classify(iToken, lObjects)

    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = index_subtype_definition.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(')', token.close_parenthesis, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)
    iCurrent = subtype_indication.classify(iCurrent, lObjects)
    return iCurrent

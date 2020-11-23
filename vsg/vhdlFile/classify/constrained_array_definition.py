
from vsg.token import constrained_array_definition as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import index_constraint
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    constrained_array_definition ::=
        array index_constraint of *element*_subtype_indication
    '''

    if utils.is_next_token('array', iToken, lObjects):
        if not utils.find_in_next_n_tokens('<>', 5, iToken, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken

    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('array', token.array_keyword, iToken, lObjects)

    iCurrent = index_constraint.classify(iToken, lObjects)

    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)

    iCurrent = utils.classify_subelement_until(';', subtype_indication, iCurrent, lObjects)
    return iCurrent

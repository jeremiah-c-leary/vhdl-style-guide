
from vsg.token import attribute_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import entity_specification
from vsg.vhdlFile.classify import expression


def detect(iToken, lObjects):
    '''
    attribute_specification ::=
        attribute attribute_designator of entity_specification is expression ;
    '''
    if utils.are_next_consecutive_tokens(['attribute', None, 'of'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('attribute', token.attribute_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.attribute_designator, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)

    iCurrent = entity_specification.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    iCurrent = expression.classify_until([';'], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)

    return iCurrent

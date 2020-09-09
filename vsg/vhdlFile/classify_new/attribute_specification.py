
from vsg.token import attribute_specification as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import entity_specification
from vsg.vhdlFile.classify_new import expression

'''
    attribute_specification ::=
        attribute attribute_designator of entity_specification is expression ;
'''


def detect(iToken, lObjects):

    if utils.is_next_token('attribute', iToken, lObjects):
        if utils.find_in_next_n_tokens('of', 3, iToken, lObjects):
            return classify(iToken, lObjects)    
        else:
            return iToken

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('attribute', token.attribute_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.attribute_designator, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)
    iCurrent = entity_specification.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    iCurrent = utils.classify_subelement_until(';', expression, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent 

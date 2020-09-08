
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import architecture_declarative_part
from vsg.vhdlFile.classify_new import architecture_statement_part

from vsg.token import architecture_body as token

'''
architecture identifier of *entity*_name is
    architecture_declarative_part
begin
    architecture_statement_part
end [ architecture ] [ *architecture*_simple_name ] ;
'''


def detect(iToken, lObjects):
    if utils.object_value_is(lObjects, iToken, 'architecture'):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = utils.detect_subelement_until('begin', architecture_declarative_part, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = utils.detect_subelement_until('end', architecture_statement_part, iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iToken, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('architecture', token.architecture_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('of', token.of_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.entity_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    return iCurrent


def classify_closing_declaration(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('architecture', token.end_architecture_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.architecture_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent

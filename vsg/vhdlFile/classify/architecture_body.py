
from vsg.token import architecture_body as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import architecture_declarative_part
from vsg.vhdlFile.classify import architecture_statement_part


def detect(iToken, lObjects):
    '''
    architecture identifier of *entity*_name is
        architecture_declarative_part
    begin
        architecture_statement_part
    end [ architecture ] [ *architecture*_simple_name ] ;
    '''

    if utils.is_next_token('architecture', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = architecture_declarative_part.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)

    iCurrent = architecture_statement_part.classify_until(['end'], iCurrent, lObjects)

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

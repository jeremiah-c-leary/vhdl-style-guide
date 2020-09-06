
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import entity_declarative_part
from vsg.vhdlFile.classify_new import entity_header
from vsg.vhdlFile.classify_new import entity_statement_part

from vsg.token import entity_declaration as token

'''
    entity_declaration ::=
        entity identifier is
            entity_header
            entity_declarative_part
        [ begin
            entity_statement_part ]
        end [ entity ] [ entity_simple_name ] ;
'''


def detect(iToken, lObjects):
    if utils.is_next_token('entity', iToken, lObjects):
        return classify(iToken, lObjects)
    else:
        return iToken


def classify(iToken, lObjects):
    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = entity_header.detect(iCurrent, lObjects)

    iCurrent = utils.detect_submodule(iCurrent, lObjects, entity_declarative_part)

    if utils.is_next_token('begin', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('begin', token.begin_keyword, iCurrent, lObjects)
        iCurrent = utils.detect_submodule(iCurrent, lObjects, entity_statement_part)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):
    iCurrent = iToken
    iCurrent = utils.assign_next_token_required('entity', token.entity_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)
    return iCurrent


def classify_closing_declaration(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('entity', token.end_entity_keyword, iCurrent, lObjects)
    if not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.entity_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent

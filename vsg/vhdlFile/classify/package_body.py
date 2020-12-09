
from vsg.token import package_body as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import package_body_declarative_part


def detect(iToken, lObjects):
    '''
    package_body ::=
        package body *package*_simple_name is
            package_body_declarative_part
        end [ package body ] [ *package*_simple_name ] ;
    '''

    if utils.are_next_consecutive_tokens(['package', 'body', None, 'is'], iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = package_body_declarative_part.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iToken, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('package', token.package_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required('body', token.body_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.package_simple_name, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    if utils.are_next_consecutive_tokens(['package'], iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required('package', token.end_package_keyword, iToken, lObjects)
        iCurrent = utils.assign_next_token_required('body', token.end_body_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_package_simple_name, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iToken, lObjects)

    return iCurrent

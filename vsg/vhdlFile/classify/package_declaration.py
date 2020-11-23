
from vsg.token import package_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import package_declarative_part
from vsg.vhdlFile.classify import package_header


def detect(iToken, lObjects):
    '''
    package_declaration ::=
        package identifier is
            package_header
            package_declarative_part
        end [ package ] [ package_simple_name ] ;
    '''

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'package'):
        if not utils.find_in_next_n_tokens('body', 5, iCurrent, lObjects):
            if not utils.find_in_next_n_tokens('new', 5, iCurrent, lObjects):
                return classify(iToken, lObjects)
        else:
            return iToken

    return iToken


def classify(iToken, lObjects):

    iCurrent = classify_opening_declaration(iToken, lObjects)

    iCurrent = package_header.detect(iCurrent, lObjects)

    iCurrent = package_declarative_part.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('package', token.package_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required('is', token.is_keyword, iCurrent, lObjects)

    return iCurrent


def classify_closing_declaration(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('end', token.end_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if('package', token.end_package_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if_not(';', token.end_package_simple_name, iToken, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iToken, lObjects)

    return iCurrent

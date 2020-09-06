
from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import package_declarative_part
from vsg.vhdlFile.classify_new import package_header

from vsg.token import package_declaration as token

'''
    package_declaration ::=
        package identifier is
            package_header
            package_declarative_part
        end [ package ] [ package_simple_name ] ;
'''


def detect(iToken, lObjects):
    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'package'):
        if not utils.find_in_next_n_tokens('body', 5, iCurrent, lObjects):
            return classify(iToken, lObjects)
        else:
            return iToken 

    return iToken


def classify(iToken, lObjects):
    iCurrent = classify_opening_declaration(iToken, lObjects)

    iLast = 0
    while iLast != iCurrent:
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iLast = iCurrent
        iCurrent = package_header.detect(iCurrent, lObjects)

    iLast = 0
    while iLast != iCurrent:
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iLast = iCurrent
        if utils.object_value_is(lObjects, iCurrent, 'end'):
             break 
        iCurrent = package_declarative_part.detect(iCurrent, lObjects)

    iCurrent = classify_closing_declaration(iCurrent, lObjects)

    return iCurrent


def classify_opening_declaration(iToken, lObjects):
    iCurrent = iToken
    iCurrent = utils.classify_next_token_if('package', token.package_keyword, iCurrent, lObjects)
    iCurrent = utils.classify_next_token(token.identifier, iCurrent, lObjects)
    iCurrent = utils.classify_next_token_if('is', token.is_keyword, iCurrent, lObjects)
    return iCurrent


def classify_closing_declaration(iToken, lObjects):
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('package', token.end_package_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_package_simple_name)

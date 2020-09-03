
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


def detect(iCurrent, lObjects):
    if utils.object_value_is(lObjects, iCurrent, 'architecture'):
        return classify(iCurrent, lObjects)
    return iCurrent


def classify(iCurrent, lObjects):

    classify_opening_declaration(iCurrent, lObjects)

    iToken = iCurrent

    iLast = 0           
    while iLast != iToken:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.classify_token('begin', token.begin_keyword, iToken, lObjects):
            iToken += 1
        else:
            iToken = architecture_declarative_part.detect(iToken, lObjects)
        
    iLast = 0           
    while iLast != iToken:
        iLast = iToken
        iToken = utils.find_next_token(iToken, lObjects)
        if not utils.object_value_is(lObjects, iToken, 'end'):
            iToken = architecture_statement_part.detect(iToken, lObjects)

    classify_closing_declaration(iToken, lObjects)

    return iToken


def classify_opening_declaration(iToken, lObjects):
    bIdentifierFound = False

    iStart, iEnd = utils.get_range(lObjects, iToken, 'is')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('architecture', token.architecture_keyword, iToken, lObjects):
            continue
        if utils.classify_token('of', token.of_keyword, iToken, lObjects):
            continue
        if utils.classify_token('is', token.is_keyword, iToken, lObjects):
            continue
        if not bIdentifierFound:
           utils.assign_token(lObjects, iToken, token.identifier)
           bIdentifierFound = True
           continue
        if bIdentifierFound:
           utils.assign_token(lObjects, iToken, token.entity_name)


def classify_closing_declaration(iToken, lObjects):
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('architecture', token.end_architecture_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.architecture_simple_name)

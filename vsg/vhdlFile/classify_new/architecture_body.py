
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

    bIdentifierFound = False
#    print('--> opening architecture')
#    print(iCurrent)
    iStart, iEnd = utils.get_range(lObjects, iCurrent, 'is')
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
#    print(iToken)
#    print('--> detecting architecture_declarative_part')
    iLast = 0           
    while iLast != iToken:
        while not utils.is_item(lObjects, iToken):
            iToken += 1
        iLast = iToken
        iToken = architecture_declarative_part.detect(iToken, lObjects)
        
#    print('--> architecture begin keyword')
    utils.classify_token('begin', token.begin_keyword, iToken, lObjects)
    iToken += 1

#    print('--> detecting architecture_statement_part')
    iLast = 0           
    while iLast != iToken:
        iLast = iToken
        iToken = utils.find_next_token(iToken, lObjects)
        if not utils.object_value_is(lObjects, iToken, 'end'):
            iToken = architecture_statement_part.detect(iToken, lObjects)
        
#    print('--> closing architecture')
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

    return iToken

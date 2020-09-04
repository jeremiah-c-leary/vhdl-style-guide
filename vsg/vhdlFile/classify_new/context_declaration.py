
from vsg import parser
from vsg.token import context_declaration as token

from vsg.vhdlFile.classify_new import context_clause

from vsg.vhdlFile import utils

'''
    context_declaration ::=
        context identifier is
            context_clause
        end [ context ] [ context_simple_name ] ;
'''

def detect(iToken, lObjects):

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.object_value_is(lObjects, iCurrent, 'context'):
        if utils.find_in_range('is', iCurrent, ';', lObjects):
            return classify(iCurrent, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.classify_next_token_if('context', token.context_keyword, iToken, lObjects)
    iCurrent = utils.classify_next_token(token.identifier, iToken, lObjects)
    iCurrent = utils.classify_next_token_if('is', token.is_keyword, iToken, lObjects)

    iLast = 0
    while iLast != iCurrent:
        iCurrent = utils.find_next_token(iToken, lObjects)
        iLast = iCurrent
        if utils.object_value_is(lObjects, iToken, 'end'):
             break 
        iCurrent = context_clause.detect(iCurrent, lObjects)


    iStart, iEnd = utils.get_range(lObjects, iCurrent, ';')
    for iToken in range(iStart, iEnd + 1):
        if utils.is_item(lObjects, iToken):
            if utils.classify_token('context', token.end_context_keyword, iToken, lObjects):
                continue
            if utils.classify_token('end', token.end_keyword, iToken, lObjects):
                continue
            if utils.classify_token(';', token.semicolon, iToken, lObjects):
                continue
            utils.assign_token(lObjects, iToken, token.context_simple_name)

    return iEnd

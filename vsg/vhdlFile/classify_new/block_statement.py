
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import block_statement as token

from vsg.vhdlFile.classify_new import block_header
from vsg.vhdlFile.classify_new import block_declarative_part
from vsg.vhdlFile.classify_new import block_statement_part

'''
    block_statement ::=
    block_label :
        block [ ( guard_condition ) ] [ is ]
            block_header
            block_declarative_part
        begin
            block_statement_part
        end block [ block_label ] ;
'''


def detect(iCurrent, lObjects):
    iItemCount = 0
    iIndex = iCurrent
    try:
        while iItemCount < 3:
            if utils.is_item(lObjects, iIndex):
                iItemCount += 1
            iIndex += 1
        else:
            if utils.object_value_is(lObjects, iIndex-1, 'block'):  # jcl - why is this iIndex - 1?
                return classify(iCurrent, lObjects)
    except IndexError:
        return iCurrent
    return iCurrent


def classify(iCurrent, lObjects):

    ### Classify opening keywords
    iStart, iEnd = utils.get_range(lObjects, iCurrent, 'block')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('block', token.keyword, iToken, lObjects):
            continue
        if utils.classify_token(':', token.label_colon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.block_label)

    ### Check for guard condition
    if utils.have_guard_condition(iToken, lObjects):
        iStart, iEnd = utils.get_range(lObjects, iToken, ')')
        for iToken in range(iStart, iEnd + 1):
            if not utils.is_item(lObjects, iToken):
                continue
            utils.assign_token(lObjects, iToken, token.guard_condition)

    ### Find next item
    iToken = utils.find_next_token(iToken, lObjects)

    ### Classify the is keyword if it exists
    iToken = utils.classify_is_keyword(iToken, token.is_keyword, lObjects)
        
    iToken = utils.detect_submodule(iToken, lObjects, block_header)
    iToken = utils.detect_submodule(iToken, lObjects, block_declarative_part)

    ### Classify Begin keyword        
    iToken = utils.classify_begin_keyword(iToken, token.begin_keyword, lObjects)

    iToken = utils.detect_submodule(iToken, lObjects, block_statement_part)

    ### Classify the closing keywords
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('block', token.end_block_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_block_label)

    return iToken


from vsg.token import context_reference as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    context_reference ::=
        context selected_name { , selected_name } ;
    '''
    if utils.object_value_is(lObjects, iCurrent, 'context'):
        if not utils.find_in_range('is', iCurrent, ';', lObjects):
            return classify(iCurrent, lObjects)
    return iCurrent


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('context', token.keyword, iToken, lObjects)
    iCurrent = classify_selected_name(iCurrent, lObjects)
    while utils.is_next_token(',', iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)
        iCurrent = classify_selected_name(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent


def classify_selected_name(iToken, lObjects):
    iTokenIndex = utils.find_next_token(iToken, lObjects)
    lTokens = lObjects[iTokenIndex].get_value().split('.')
    if lObjects[iTokenIndex + 1].get_value().startswith('"'):
        lTokens[-1] = lObjects.pop(iTokenIndex + 1).get_value()
    lNewTokens = build_selected_name_token_list(lTokens)
    replace_item_in_list_with_a_list_at_index(lObjects, lNewTokens, iTokenIndex)
    iNewIndex = iToken + len(lNewTokens)
    
    return iNewIndex


def build_selected_name_token_list(lTokens):
    lNewTokens = []
    for iThisToken, sToken in enumerate(lTokens):
        classify_selected_name_elements(iThisToken, sToken, lNewTokens, lTokens)
    lNewTokens.pop()
    return lNewTokens


def classify_selected_name_elements(iThisToken, sToken, lNewTokens, lTokens):
    if iThisToken == 0 and len(lTokens) > 1:
        lNewTokens.append(token.library_name(sToken))
    else:
        lNewTokens.append(token.context_name(sToken))
    lNewTokens.append(token.dot())


def replace_item_in_list_with_a_list_at_index(lFirstList, lSecondList, iIndex):
    lFirstList.pop(iIndex)
    lSecondList.reverse()
    for oToken in lSecondList:
        lFirstList.insert(iIndex, oToken)

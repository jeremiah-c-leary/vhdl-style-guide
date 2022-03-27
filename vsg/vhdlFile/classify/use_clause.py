
from vsg.token import use_clause as token

from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    '''
    use_clause ::=
        use selected_name { , selected_name } ;
    '''
    if utils.is_next_token('use', iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):

    iCurrent = utils.assign_next_token_required('use', token.keyword, iToken, lObjects)

    while not utils.is_next_token(';', iCurrent, lObjects):
        iCurrent = classify_selected_name(iCurrent, lObjects)
    
        if utils.is_next_token(',', iCurrent, lObjects):
            iCurrent = utils.assign_next_token_required(',', token.comma, iCurrent, lObjects)

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
        if iThisToken == 0:
            lNewTokens.append(token.library_name(sToken))
        elif sToken.lower() == 'all':
            lNewTokens.append(token.all_keyword(sToken))
        elif iThisToken == len(lTokens) - 1:
            lNewTokens.append(token.item_name(sToken))
        else:
            lNewTokens.append(token.package_name(sToken))
        lNewTokens.append(token.dot())
    lNewTokens.pop()
    return lNewTokens


def replace_item_in_list_with_a_list_at_index(lFirstList, lSecondList, iIndex):
    lFirstList.pop(iIndex)
    lSecondList.reverse()
    for oToken in lSecondList:
        lFirstList.insert(iIndex, oToken)

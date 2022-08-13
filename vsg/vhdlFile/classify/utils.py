
from vsg.vhdlFile import utils


def classify_selected_name(iToken, lObjects, token):
    iTokenIndex = utils.find_next_token(iToken, lObjects)
    lTokens = lObjects[iTokenIndex].get_value().split('.')
    if lObjects[iTokenIndex + 1].get_value().startswith('"'):
        lTokens[-1] = lObjects.pop(iTokenIndex + 1).get_value()
    lNewTokens = build_selected_name_token_list(lTokens, token)
    replace_item_in_list_with_a_list_at_index(lObjects, lNewTokens, iTokenIndex)
    iNewIndex = iToken + len(lNewTokens)

    return iNewIndex


def build_selected_name_token_list(lTokens, token):
    if is_use_clause_selected_name(token):
        return build_use_clause_selected_name_token_list(lTokens, token)
    return build_context_reference_selected_name_token_list(lTokens, token)


def build_use_clause_selected_name_token_list(lTokens, token):
    lNewTokens = []
    for iThisToken, sToken in enumerate(lTokens):
        classify_use_clause_selected_name_elements(iThisToken, lNewTokens, lTokens, token)
    lNewTokens.pop()
    return lNewTokens


def build_context_reference_selected_name_token_list(lTokens, token):
    lNewTokens = []
    for iThisToken, sToken in enumerate(lTokens):
        classify_context_reference_selected_name_elements(iThisToken, lNewTokens, lTokens, token)
    lNewTokens.pop()
    return lNewTokens


def classify_use_clause_selected_name_elements(iThisToken, lNewTokens, lTokens, token):
    sToken = lTokens[iThisToken]
    if iThisToken == 0:
        lNewTokens.append(token.library_name(sToken))
    elif sToken.lower() == 'all':
        lNewTokens.append(token.all_keyword(sToken))
    elif iThisToken == len(lTokens) - 1:
        lNewTokens.append(token.item_name(sToken))
    else:
        lNewTokens.append(token.package_name(sToken))
    lNewTokens.append(token.dot())


def classify_context_reference_selected_name_elements(iThisToken, lNewTokens, lTokens, token):
    sToken = lTokens[iThisToken]
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


def is_use_clause_selected_name(token):
    if token.__name__ == 'vsg.token.use_clause':
        return True
    return False


def classify_production(production, iToken, lObjects):
    iCurrent = iToken
    iStop = len(lObjects)
    while iCurrent < iStop:
        iPrevious = iCurrent
        iCurrent = production.detect(iCurrent, lObjects)
        if iPrevious == iCurrent:
            break
    return iCurrent

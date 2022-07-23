
from vsg import parser
from vsg.token import delimited_comment as token


def classify(lTokens, lObjects, oOptions):

    for iToken, sToken in enumerate(lTokens):
        if not oOptions.inside_delimited_comment():
            if sToken.startswith('--'):
                lObjects[iToken] = parser.comment(sToken)
            if sToken == '/*':
                lObjects[iToken] = token.beginning(sToken)
                oOptions.set_inside_delimited_comment()
        else:
            if sToken == '*/':
                lObjects[iToken] = token.ending(sToken)
                oOptions.clear_inside_delimited_comment()
            else:
                lObjects[iToken] = token.text(sToken)

    if len(lObjects) == 0 and oOptions.inside_delimited_comment():
        lObjects.append(token.text(''))

    merge_text_tokens(lObjects)


def merge_text_tokens(lObjects):

    iStartIndex, iEndIndex = find_start_and_end_index_of_text_tokens(lObjects)
    merge_tokens(iStartIndex, iEndIndex, lObjects)


def find_start_and_end_index_of_text_tokens(lObjects):
    iStartIndex = -1
    iEndIndex = -1
    for iToken, oToken in enumerate(lObjects):
        iStartIndex = set_start_index(oToken, iToken, iStartIndex)
        iEndIndex = set_end_index(oToken, iToken, iEndIndex)
    return iStartIndex, iEndIndex


def set_start_index(oToken, iToken, iStartIndex):
    if isinstance(oToken, token.text):
        if iStartIndex == -1:
            iStartIndex = iToken
    return iStartIndex


def set_end_index(oToken, iToken, iEndIndex):
    if isinstance(oToken, token.text):
        iEndIndex = iToken
    return iEndIndex


def merge_tokens(iStartIndex, iEndIndex, lObjects):
    if iStartIndex < iEndIndex:
        sNewValue = ''
        for iIndex in range(iStartIndex, iEndIndex + 1):
            sNewValue += lObjects[iIndex].get_value()
        del lObjects[iStartIndex:iEndIndex + 1]
        lObjects.insert(iStartIndex, token.text(sNewValue))

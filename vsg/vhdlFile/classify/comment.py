
from vsg import parser
from vsg.token import delimited_comment as token


def classify(lTokens, lObjects, oOptions):

    if len(lObjects) == 0 and oOptions.inside_delimited_comment():
        lObjects.append(token.text(''))

    for iToken, sToken in enumerate(lTokens):
        classify_delimited_comment_text(iToken, lObjects, oOptions)
        classify_opening_comment_delimiters(iToken, lObjects, oOptions)
        classify_closing_comment_delimiters(iToken, lObjects, oOptions)

    merge_text_tokens(lObjects)


def classify_closing_comment_delimiters(iToken, lObjects, oOptions):
    sToken = lObjects[iToken].get_value()
    if oOptions.inside_delimited_comment() and sToken == '*/':
        lObjects[iToken] = token.ending(sToken)
        oOptions.clear_inside_delimited_comment()


def classify_opening_comment_delimiters(iToken, lObjects, oOptions):
    classify_single_line_comment(iToken, lObjects, oOptions)
    classify_delimited_comment_open_keyword(iToken, lObjects, oOptions)


def classify_single_line_comment(iToken, lObjects, oOptions):
    sToken = lObjects[iToken].get_value()
    if not oOptions.inside_delimited_comment() and sToken.startswith('--'):
        lObjects[iToken] = parser.comment(sToken)


def classify_delimited_comment_open_keyword(iToken, lObjects, oOptions):
    sToken = lObjects[iToken].get_value()
    if not oOptions.inside_delimited_comment() and sToken == '/*':
        lObjects[iToken] = token.beginning(sToken)
        oOptions.set_inside_delimited_comment()


def classify_delimited_comment_text(iToken, lObjects, oOptions):
    sToken = lObjects[iToken].get_value()
    if oOptions.inside_delimited_comment():
        lObjects[iToken] = token.text(sToken)


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
    if isinstance(oToken, token.text) and iStartIndex == -1:
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

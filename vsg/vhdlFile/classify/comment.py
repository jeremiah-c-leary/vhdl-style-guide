
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

    iStartIndex = -1
    iEndIndex = -1
    for iToken, sToken in enumerate(lObjects):
        if isinstance(lObjects[iToken], token.text):
            if iStartIndex == -1:
                iStartIndex = iToken
            iEndIndex = iToken

    if iStartIndex < iEndIndex:
        sNewValue = ''
        for iIndex in range(iStartIndex, iEndIndex + 1):
            sNewValue += lObjects[iIndex].get_value()
        del lObjects[iStartIndex:iEndIndex + 1]
        lObjects.insert(iStartIndex, token.text(sNewValue))

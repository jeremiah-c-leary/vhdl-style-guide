

from vsg import parser


def classify(lTokens, lObjects):
    '''
    Classifies whitespace objects.

    '''
    # Check for entity
    for iToken, sToken in enumerate(lTokens):
        if ' ' in sToken:
            if sToken[0] == '"' and sToken[-1] == '"':
                pass
            else:
                lObjects[iToken] = parser.whitespace(sToken)

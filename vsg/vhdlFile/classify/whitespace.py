

from vsg import parser


def whitespace(lTokens, lObjects):
    '''
    Classifies whitespace objects.

    '''
    # Check for entity
    for iToken, sToken in enumerate(lTokens):
        if ' ' in sToken:
            lObjects[iToken] = parser.whitespace(sToken)

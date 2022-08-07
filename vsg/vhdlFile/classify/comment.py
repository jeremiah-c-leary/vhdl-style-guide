
from vsg import parser


def classify(lTokens, lObjects):

    for iToken, sToken in enumerate(lTokens):
        if sToken.startswith('--'):
            lObjects[iToken] = parser.comment(sToken)
            if '\t' in sToken:
                lObjects[iToken].has_tab = True

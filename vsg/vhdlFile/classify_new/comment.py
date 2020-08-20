
from vsg import parser

def classify(dVars, lTokens, lObjects, oLine):
    
    for iToken, sToken in enumerate(lTokens):
        if sToken.startswith('--'):
            lObjects[iToken] = parser.comment(sToken)

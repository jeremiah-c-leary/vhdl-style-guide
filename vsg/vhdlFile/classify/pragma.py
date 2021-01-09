
from vsg import parser

from vsg.token import pragma


def classify(lTokens, lObjects, lOpenPragmas, lClosePragmas, dVars):
    '''
    Classifies pragmas

    '''
    for iToken, sToken in enumerate(lTokens):
        if sToken in lClosePragmas:
            dVars['pragma'] = False
        if dVars['pragma']:
            if isinstance(lObjects[iToken], parser.item):
                lObjects[iToken] = pragma.ignore(sToken)
        if sToken in lOpenPragmas:
            dVars['pragma'] = True

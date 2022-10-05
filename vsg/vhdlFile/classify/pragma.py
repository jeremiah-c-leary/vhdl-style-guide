
from vsg import parser

from vsg.token import pragma


def classify(lTokens, lObjects, lOpenPragmas, lClosePragmas, dVars):
    '''
    Classifies pragmas

    '''
    for iToken, sToken in enumerate(lTokens):
        if sToken in lOpenPragmas:
            dVars['pragma'] = True
        if dVars['pragma']:
            if not isinstance(lObjects[iToken], parser.whitespace):
                lObjects[iToken] = pragma.ignore(sToken)
        if sToken in lClosePragmas:
            dVars['pragma'] = False

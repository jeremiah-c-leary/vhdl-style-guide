
from vsg import parser

from vsg.token import pragma


def classify(lTokens, lObjects, lOpenPragmas, lClosePragmas, dVars, configuration):
    '''
    Classifies pragmas

    '''
    if not dVars['pragma']: 
       lPragmaRegex = configuration.dConfig['pragma']['regexp']
       sLine = ''.join(lTokens)
       for regex in lPragmaRegex:
           if regex.match(sLine):
               for iToken, sToken in enumerate(lTokens):
                   if isinstance(lObjects[iToken], parser.comment):
                       lObjects[iToken] = pragma.pragma(sToken)

    for iToken, sToken in enumerate(lTokens):
        if sToken in lOpenPragmas:
            dVars['pragma'] = True
        if dVars['pragma']:
            if not isinstance(lObjects[iToken], parser.whitespace):
                lObjects[iToken] = pragma.ignore(sToken)
        if sToken in lClosePragmas:
            dVars['pragma'] = False



from vsg import parser

from vsg.token import pragma


def classify(lTokens, lObjects, lOpenPragmas, lClosePragmas, dVars, configuration):
    '''
    Classifies pragmas

    '''
    if not inside_vhdloff_vhdlon_region(dVars) and line_starts_with_comment(lTokens):
        classify_pragmas(lTokens, lObjects, dVars, configuration)
        check_for_open_pragmas(lTokens, dVars, lOpenPragmas)

    if inside_vhdloff_vhdlon_region(dVars):
        set_tokens_to_ignore(lTokens, lObjects, lClosePragmas, dVars)


def set_tokens_to_ignore(lTokens, lObjects, lClosePragmas, dVars):
    for iToken, sToken in enumerate(lTokens):
        if not isinstance(lObjects[iToken], parser.whitespace):
            lObjects[iToken] = pragma.ignore(sToken)
        if sToken in lClosePragmas:
            dVars['pragma'] = False


def inside_vhdloff_vhdlon_region(dVars):
    return dVars['pragma']


def line_starts_with_comment(lTokens):
    return first_token_is_a_comment(lTokens) or second_token_is_a_comment(lTokens)


def check_for_open_pragmas(lTokens, dVars, lOpenPragmas):
    for sToken in lTokens:
        if sToken in lOpenPragmas:
            dVars['pragma'] = True
        

def first_token_is_a_comment(lTokens):
    try:
        return token_is_a_comment(lTokens[0])
    except IndexError:
        return False


def second_token_is_a_comment(lTokens):
    try:
        return token_is_a_comment(lTokens[1])
    except IndexError:
        return False


def token_is_a_comment(sToken):
    if sToken.startswith('--'):
        return True
    return False


def classify_pragmas(lTokens, lObjects, dVars, configuration):
    if classify_open_pragmas(lTokens, lObjects, dVars, configuration):
        return True
    if classify_close_pragmas(lTokens, lObjects, dVars, configuration):
        return True
    if classify_single_pragmas(lTokens, lObjects, dVars, configuration):
        return True
    return False


def classify_open_pragmas(lTokens, lObjects, dVars, configuration):
    for regex in configuration.dConfig['pragma']['regexp']['open']:
        if regex.match(dVars['line']):
            for iToken, sToken in enumerate(lTokens):
                if isinstance(lObjects[iToken], parser.comment):
                    lObjects[iToken] = pragma.open(sToken)
            return True
    return False


def classify_close_pragmas(lTokens, lObjects, dVars, configuration):
    for regex in configuration.dConfig['pragma']['regexp']['close']:
        if regex.match(dVars['line']):
            for iToken, sToken in enumerate(lTokens):
                if isinstance(lObjects[iToken], parser.comment):
                    lObjects[iToken] = pragma.close(sToken)
            return True
    return False


def classify_single_pragmas(lTokens, lObjects, dVars, configuration):
    for regex in configuration.dConfig['pragma']['regexp']['single']:
        if classify_pragma(lTokens, lObjects, dVars, regex, pragma.single):
            return True
    return False


def classify_pragma(lTokens, lObjects, dVars, regex, oType):
    if regex.match(dVars['line']):
        for iToken, sToken in enumerate(lTokens):
            if isinstance(lObjects[iToken], parser.comment):
                lObjects[iToken] = pragma.single(sToken)
                return True 
    return False


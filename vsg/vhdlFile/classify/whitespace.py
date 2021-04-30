

from vsg import parser


def classify(lTokens, lObjects):
    '''
    Classifies whitespace objects.
    '''
    for iToken, sToken in enumerate(lTokens):
        if string_contains_space(sToken):
            if is_string_literal(sToken):
                pass
            elif is_character_literal(sToken):
                pass
            else:
                lObjects[iToken] = parser.whitespace(sToken)


def string_contains_space(sToken):
    if ' ' in sToken:
        return True
    return False


def is_string_literal(sToken):
    if sToken[0] == '"' and sToken[-1] == '"':
        return True
    return False


def is_character_literal(sToken):
    if sToken[0] == "'" and sToken[-1] == "'":
        return True
    return False

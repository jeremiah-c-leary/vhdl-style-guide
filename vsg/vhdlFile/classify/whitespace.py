# -*- coding: utf-8 -*-


from vsg import parser
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def classify(lTokens, lObjects):
    """
    Classifies whitespace objects.
    """
    for iToken, sToken in enumerate(lTokens):
        if string_contains_space(sToken):
            if is_string_literal(sToken):
                pass
            elif is_character_literal(sToken):
                pass
            else:
                lObjects[iToken] = parser.whitespace(sToken)
                if string_contains_tab(sToken):
                    lObjects[iToken].has_tab = True
        elif string_contains_tab(sToken):
            lObjects[iToken] = parser.whitespace(sToken)
            lObjects[iToken].has_tab = True


@decorators.print_classifier_debug_info(__name__)
def string_contains_space(sToken):
    if " " in sToken:
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def string_contains_tab(sToken):
    if "\t" in sToken:
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def is_string_literal(sToken):
    if sToken[0] == '"' and sToken[-1] == '"':
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def is_character_literal(sToken):
    if sToken[0] == "'" and sToken[-1] == "'":
        return True
    return False

# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import pragma


def classify(lObjects, lOpenPragmas, lClosePragmas, dVars, configuration):
    """
    Classifies pragmas

    """
    if not inside_vhdloff_vhdlon_region(dVars) and line_starts_with_comment(lObjects):
        classify_pragmas(lObjects, dVars, configuration)
        check_for_open_pragmas(lObjects, dVars, lOpenPragmas)

    if inside_vhdloff_vhdlon_region(dVars):
        set_tokens_to_ignore(lObjects, lClosePragmas, dVars)


def set_tokens_to_ignore(lObjects, lClosePragmas, dVars):
    for iToken, oToken in enumerate(lObjects):
        if not isinstance(oToken, parser.whitespace):
            lObjects[iToken] = pragma.ignore(oToken.get_value())
        if oToken.get_value() in lClosePragmas:
            dVars["pragma"] = False


def inside_vhdloff_vhdlon_region(dVars):
    return dVars["pragma"]


def line_starts_with_comment(lObjects):
    return first_token_is_a_comment(lObjects) or second_token_is_a_comment(lObjects)


def check_for_open_pragmas(lObjects, dVars, lOpenPragmas):
    for oToken in lObjects:
        sToken = oToken.get_value()
        if sToken in lOpenPragmas:
            dVars["pragma"] = True


def first_token_is_a_comment(lObjects):
    try:
        return token_is_a_comment(lObjects[0])
    except IndexError:
        return False


def second_token_is_a_comment(lObjects):
    try:
        return token_is_a_comment(lObjects[1])
    except IndexError:
        return False


def token_is_a_comment(oToken):
    if oToken.get_value().startswith("--"):
        return True
    return False


def classify_pragmas(lObjects, dVars, configuration):
    if classify_open_pragmas(lObjects, dVars, configuration):
        return True
    if classify_close_pragmas(lObjects, dVars, configuration):
        return True
    if classify_single_pragmas(lObjects, dVars, configuration):
        return True
    return False


def classify_open_pragmas(lObjects, dVars, configuration):
    for regex in configuration.dConfig["pragma"]["regexp"]["open"]:
        if regex.match(dVars["line"]):
            for iToken, oToken in enumerate(lObjects):
                if isinstance(oToken, parser.comment):
                    lObjects[iToken] = pragma.open(oToken.get_value())
            return True
    return False


def classify_close_pragmas(lObjects, dVars, configuration):
    for regex in configuration.dConfig["pragma"]["regexp"]["close"]:
        if regex.match(dVars["line"]):
            for iToken, oToken in enumerate(lObjects):
                if isinstance(oToken, parser.comment):
                    lObjects[iToken] = pragma.close(oToken.get_value())
            return True
    return False


def classify_single_pragmas(lObjects, dVars, configuration):
    for regex in configuration.dConfig["pragma"]["regexp"]["single"]:
        if classify_pragma(lObjects, dVars, regex, pragma.single):
            return True
    return False


def classify_pragma(lObjects, dVars, regex, oType):
    if regex.match(dVars["line"]):
        for iToken, oToken in enumerate(lObjects):
            if isinstance(oToken, parser.comment):
                lObjects[iToken] = pragma.single(oToken.get_value())
                return True
    return False

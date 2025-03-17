# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_subprogram_default as token
from vsg.vhdlFile import utils


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    interface_subprogram_default ::=
        *subprogram*_name | <>
    """
    if utils.is_next_token("<>", iToken, lObjects):
        return utils.assign_next_token_required("<>", token.undefined_range, iToken, lObjects)
    return utils.classify_next_token(token.subprogram_name, iToken, lObjects)

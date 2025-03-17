# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import force_mode as token
from vsg.vhdlFile import utils


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    force_mode ::=
        in | out
    """

    iCurrent = utils.assign_next_token_if("in", token.in_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("out", token.out_keyword, iCurrent, lObjects)

    return iCurrent

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import force_mode as token


# TODO:  Split detect into detect and classify
@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    force_mode ::=
        in | out
    """

    oDataStructure.replace_next_token_with_if("in", token.in_keyword)
    oDataStructure.replace_next_token_with_if("out", token.out_keyword)

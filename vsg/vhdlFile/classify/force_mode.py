# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import force_mode as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    force_mode ::=
        in | out
    """

    if oDataStructure.is_next_token_one_of(["in", "out"]):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("in", token.in_keyword)
    oDataStructure.replace_next_token_with_if("out", token.out_keyword)

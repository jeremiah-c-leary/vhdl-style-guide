# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import mode as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    mode ::=
        in | out | inout | buffer | linkage
    """

    oDataStructure.replace_next_token_with_if("in", token.in_keyword)
    oDataStructure.replace_next_token_with_if("out", token.out_keyword)
    oDataStructure.replace_next_token_with_if("inout", token.inout_keyword)
    oDataStructure.replace_next_token_with_if("buffer", token.buffer_keyword)
    oDataStructure.replace_next_token_with_if("linkage", token.linkage_keyword)

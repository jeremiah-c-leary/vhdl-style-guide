# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import index_subtype_definition as token
from vsg.vhdlFile.classify import type_mark


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    index_subtype_definition ::=
        type_mark range <>
    """

    type_mark.classify(oDataStructure)
    oDataStructure.replace_next_token_required("range", token.range_keyword)
    oDataStructure.replace_next_token_required("<>", token.undefined_range)

# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import attribute_name as token
from vsg.vhdlFile.classify import expression, prefix, signature


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    attribute_name ::=
        prefix [ signature ] ' attribute_designator [ ( expression ) ]
    """

    skip_prefix(oDataStructure)

    if signature.detect(oDataStructure):
        return True

    if oDataStructure.is_next_seek_token("'"):
        return True

    return False


@decorators.print_classifier_debug_info(__name__)
def skip_prefix(oDataStructure):
    oDataStructure.advance_to_next_seek_token()
    oDataStructure.increment_seek_index()
    oDataStructure.advance_seek_over_parenthesis()


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    prefix.classify(oDataStructure, token)

    if signature.detect(oDataStructure):
        signature.classify(oDataStructure)

    oDataStructure.replace_next_token_required("'", token.tic)
    oDataStructure.replace_next_token_with(token.attribute)

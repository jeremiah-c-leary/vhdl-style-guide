# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import file_type_definition as token
from vsg.vhdlFile.classify import type_mark


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    file_type_definition ::=
        file of type_mark
    """

    if oDataStructure.is_next_token("file"):
        classify(oDataStructure)
        return True

    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.file_keyword)
    oDataStructure.replace_next_token_required("of", token.of_keyword)

    type_mark.classify(oDataStructure)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import file_open_information as token
from vsg.vhdlFile.classify import file_logical_name


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    file_open_information ::=
        [ open *file_open_kind*_expression ] is file_logical_name
    """

    if oDataStructure.is_next_token_one_of(["open", "is"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.is_next_token("open"):
        oDataStructure.replace_next_token_with(token.open_keyword)
        oDataStructure.replace_next_token_with(token.file_open_kind_expression)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    file_logical_name.classify(oDataStructure)

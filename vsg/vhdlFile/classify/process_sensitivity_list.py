# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import process_sensitivity_list as token
from vsg.vhdlFile.classify import sensitivity_list


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    process_sensitivity_list ::=
        all | sensitivity_list
    """

    if oDataStructure.is_next_token("all"):
        oDataStructure.replace_next_token_with(token.all_keyword)
    else:
        sensitivity_list.classify(oDataStructure)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import sensitivity_clause as token
from vsg.vhdlFile.classify import sensitivity_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    sensitivity_clause ::=
        on sensitivity_list
    """

    if oDataStructure.is_next_token("on"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    oDataStructure.replace_next_token_required("on", token.on_keyword)

    sensitivity_list.classify_until(lUntils, oDataStructure)

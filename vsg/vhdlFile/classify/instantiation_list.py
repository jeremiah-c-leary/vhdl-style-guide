# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import instantiation_list as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    instantiation_list ::=
        instantiation_label { , instantiation_label }
      | **others**
      | **all**
    """
    if oDataStructure.is_next_token("others"):
        oDataStructure.replace_next_token_required("others", token.others_keyword)

    elif oDataStructure.is_next_token("all"):
        oDataStructure.replace_next_token_required("all", token.all_keyword)

    else:
        oDataStructure.replace_next_token_with(token.instantiation_label)

        while oDataStructure.is_next_token(","):
            oDataStructure.replace_next_token_required(",", token.comma)
            oDataStructure.replace_next_token_with(token.instantiation_label)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import entity_specification as token
from vsg.vhdlFile.classify import entity_name_list


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    entity_specification ::=
        entity_name_list : entity_class
    """

    entity_name_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(":", token.colon)

    oDataStructure.replace_next_token_with(token.entity_class)

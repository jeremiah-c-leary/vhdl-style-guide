# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import entity_name_list as token
from vsg.vhdlFile.classify import entity_designator


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    entity_name_list ::=
        entity_designator { , entity_designator }
      | others
      | all
    """

    if oDataStructure.is_next_token("others"):
        oDataStructure.replace_next_token_with(token.others_keyword)

    elif oDataStructure.is_next_token("all"):
        oDataStructure.replace_next_token_with(token.all_keyword)

    else:
        entity_designator.classify(oDataStructure)

        while oDataStructure.is_next_token(","):
            oDataStructure.replace_next_token_with(token.comma)
            entity_designator.classify(oDataStructure)

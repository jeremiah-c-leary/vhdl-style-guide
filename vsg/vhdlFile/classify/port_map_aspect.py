# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import port_map_aspect as token
from vsg.vhdlFile.classify import association_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    port_map_aspect ::=
        port map ( *port*_association_list )
    """

    if oDataStructure.are_next_consecutive_tokens(["port", "map", "("]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.port_keyword)
    oDataStructure.replace_next_token_with(token.map_keyword)
    oDataStructure.replace_next_token_with(token.open_parenthesis)

    association_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)

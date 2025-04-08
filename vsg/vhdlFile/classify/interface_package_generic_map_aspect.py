# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_package_generic_map_aspect as token
from vsg.vhdlFile.classify import generic_map_aspect


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_package_generic_map_aspect ::=
        generic_map_aspect
      | generic map ( <> )
      | generic map ( default )
    """
    if oDataStructure.are_next_consecutive_tokens(["generic", "map", "(", "<>"]):
        classify(oDataStructure)
        return True
    elif oDataStructure.are_next_consecutive_tokens(["generic", "map", "(", "default"]):
        classify(oDataStructure)
        return True
    else:
        return generic_map_aspect.detect(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("generic", token.generic_keyword)
    oDataStructure.replace_next_token_required("map", token.map_keyword)
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)
    oDataStructure.replace_next_token_with_if("default", token.default_keyword)
    oDataStructure.replace_next_token_with_if("<>", token.undefined_range)
    oDataStructure.replace_next_token_required(")", token.close_parenthesis)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import unbounded_array_definition as token
from vsg.vhdlFile.classify import index_subtype_definition, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    unbounded_array_definition ::=
        array ( index_subtype_definition { , index_subtype_definition } )
            of *element*_subtype_indication
    """

    if oDataStructure.is_next_seek_token("array"):
        if oDataStructure.does_string_exist_in_next_n_tokens("<>", 5):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.array_keyword)
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)
    index_subtype_definition.classify(oDataStructure)

    while oDataStructure.is_next_seek_token(","):
        oDataStructure.replace_next_token_with(token.comma)
        index_subtype_definition.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    oDataStructure.replace_next_token_required("of", token.of_keyword)
    subtype_indication.classify(oDataStructure)

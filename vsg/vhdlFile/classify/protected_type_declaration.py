# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import protected_type_declaration as token
from vsg.vhdlFile.classify import protected_type_declarative_part


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    protected_type_declaration ::=
        **protected**
        protected_type_declarative_part
        **end** **protected** [ protected_type_simple_name ]
    """

    if oDataStructure.is_next_token("protected"):
        if not oDataStructure.are_next_consecutive_tokens(["protected", "body"]):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("protected", token.protected_keyword)

    protected_type_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("protected", token.end_protected_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.protected_type_simple_name)

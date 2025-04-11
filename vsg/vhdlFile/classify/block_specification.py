# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import block_specification as token
from vsg.vhdlFile.classify import generate_specification


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    block_specification ::=
        architecture_name
      | block_statement_label
      | generate_statement_label [ ( generate_specification ) ]
    """

    if oDataStructure.does_string_exist_in_next_n_tokens("(", 2):
        oDataStructure.replace_next_token_with(token.generate_statement_label)
        oDataStructure.replace_next_token_required("(", token.open_parenthesis)
        generate_specification.classify(oDataStructure)
        oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    else:
        oDataStructure.replace_next_token_with(token.architecture_name)

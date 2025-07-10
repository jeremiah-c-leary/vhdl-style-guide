# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import case_generate_alternative as token
from vsg.vhdlFile.classify import choices, generate_statement_body, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    case_generate_alternative ::=
        when [ alternative_label : ] choices =>
            generate_statement_body
    """

    if oDataStructure.is_next_token("when"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("when", token.when_keyword)

    utils.tokenize_label(oDataStructure, token.alternative_label_name, token.alternative_label_colon)

    choices.classify_until(["=>"], oDataStructure)

    oDataStructure.replace_next_token_required("=>", token.assignment)

    generate_statement_body.classify(oDataStructure)

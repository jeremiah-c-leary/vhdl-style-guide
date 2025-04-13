# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import fairness_statement as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    [ label : ] Fairness_Statement

    Cover_Directive ::=
        fairness Boolean ;
      | strong fairness Boolean, Boolean ;
    """

    if (
        oDataStructure.are_next_consecutive_tokens([None, ":", "fairness"])
        or oDataStructure.is_next_token("fairness")
        or oDataStructure.are_next_consecutive_tokens([None, ":", "strong", "fairness"])
        or oDataStructure.are_next_consecutive_tokens(["strong", "fairness"])
    ):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("strong", token.strong_keyword)
    oDataStructure.replace_next_token_required("fairness", token.fairness_keyword)

    utils.assign_tokens_until(";", token.todo, oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import exit_statement as token
from vsg.vhdlFile.classify import condition, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    exit_statement ::=
        [ label : ] exit [ loop_label ] [ when condition ] ;
    """

    if utils.keyword_found("exit", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)

    oDataStructure.replace_next_token_required("exit", token.exit_keyword)

    if not oDataStructure.is_next_token_one_of([";", "when"]):
        oDataStructure.replace_next_token_with(token.loop_label)

    if oDataStructure.is_next_token("when"):
        oDataStructure.replace_next_token_with(token.when_keyword)
        condition.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

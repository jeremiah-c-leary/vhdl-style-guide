# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import next_statement as token
from vsg.vhdlFile.classify import condition, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    next_statement ::=
        [ label : ] next [ loop_label ] [ when condition ] ;
    """
    if utils.keyword_found("next", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)
    oDataStructure.replace_next_token_required("next", token.next_keyword)

    if not oDataStructure.is_next_token(";") and not oDataStructure.is_next_token("when"):
        utils.assign_next_token(token.loop_label, oDataStructure)

    if oDataStructure.is_next_token("when"):
        oDataStructure.replace_next_token_required("when", token.when_keyword)
        condition.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import null_statement as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    null_statement ::=
        [ label : ] null ;
    """
    if utils.keyword_found("null", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)
    oDataStructure.replace_next_token_required("null", token.null_keyword)
    oDataStructure.replace_next_token_required(";", token.semicolon)

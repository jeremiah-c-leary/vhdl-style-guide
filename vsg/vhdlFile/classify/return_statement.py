# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import return_statement as token
from vsg.vhdlFile.classify import expression, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    return_statement ::=
        [ label : ] return [ expression ] ;
    """

    if utils.keyword_found("return", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)

    oDataStructure.replace_next_token_required("return", token.return_keyword)

    if not oDataStructure.is_next_token(";"):
        expression.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

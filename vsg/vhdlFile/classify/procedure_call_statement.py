# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import procedure_call_statement as token
from vsg.vhdlFile.classify import procedure_call, utils

lKeywords = ["null", "return", "exit", "next", "while", "for", "loop", "case", "if", "report", "assert", "wait", "end", "with", "else", "elsif", "when"]


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    procedure_call_statement ::=
        [ label : ] procedure_call ;
    """

    if procedure_call.detect(oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label, token.label_colon)

    procedure_call.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

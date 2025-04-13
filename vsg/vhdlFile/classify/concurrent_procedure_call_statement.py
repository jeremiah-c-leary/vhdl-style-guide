# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import concurrent_procedure_call_statement as token
from vsg.vhdlFile.classify import procedure_call, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;
    """

    if procedure_call.detect(oDataStructure):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.label_name, token.label_colon)

    oDataStructure.replace_next_token_with_if("postponed", token.postponed_keyword)

    procedure_call.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import loop_statement as token
from vsg.vhdlFile.classify import iteration_scheme, sequence_of_statements, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    loop_statement ::=
        [ loop_label : ]
            [ iteration_scheme ] loop
                sequence_of_statements
            end loop [ loop_label ] ;
    """
    oDataStructure.align_seek_index()
    if oDataStructure.are_next_consecutive_tokens([None, ":"]):
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()

    if oDataStructure.is_next_seek_token("loop"):
        classify(oDataStructure)
        return True
    if iteration_scheme.detect(oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.loop_label, token.label_colon)

    iteration_scheme.classify(oDataStructure)

    oDataStructure.replace_next_token_required("loop", token.loop_keyword)

    sequence_of_statements.detect(oDataStructure, "end")

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("loop", token.end_loop_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_loop_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)

# -*- coding: utf-8 -*-

from vsg.token import loop_statement as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import iteration_scheme, sequence_of_statements


def detect(oDataStructure):
    """
    loop_statement ::=
        [ loop_label : ]
            [ iteration_scheme ] loop
                sequence_of_statements
            end loop [ loop_label ] ;
    """
    oDataStructure.align_seek_index()
    if oDataStructure.does_string_exist_in_next_n_tokens(":", 2):
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
        oDataStructure.increment_seek_index()

    if oDataStructure.is_next_seek_token("loop"):
        classify(oDataStructure)
        return True
    if iteration_scheme.detect(oDataStructure):
        classify(oDataStructure)
        return True
    return False


def classify(iToken, lObjects):
    iCurrent = utils.tokenize_label(iToken, lObjects, token.loop_label, token.label_colon)

    iCurrent = iteration_scheme.classify(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("loop", token.loop_keyword, iCurrent, lObjects)

    iCurrent = sequence_of_statements.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("end", token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("loop", token.end_loop_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(";", token.end_loop_label, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent

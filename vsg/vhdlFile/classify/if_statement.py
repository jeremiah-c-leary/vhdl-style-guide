# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import if_statement as token
from vsg.vhdlFile.classify import condition, sequence_of_statements, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    if_statement ::=
        [ if_label : ]
            if condition then
                sequence_of_statements
            { elsif condition then
                sequence_of_statements }
            [ else
                sequence_of_statements ]
            end if [ if_label ] ;
    """
    if utils.keyword_found("if", oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.if_label, token.label_colon)
    oDataStructure.replace_next_token_required("if", token.if_keyword)
    condition.classify_until(["then"], oDataStructure)
    oDataStructure.replace_next_token_required("then", token.then_keyword)

    sequence_of_statements.detect(oDataStructure, ["elsif", "else", "end"])

    while oDataStructure.is_next_token_one_of(["else", "elsif"]):
        if oDataStructure.is_next_token("elsif"):
            classify_elsif(oDataStructure)
        else:
            classify_else(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("if", token.end_if_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_if_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)


@decorators.print_classifier_debug_info(__name__)
def classify_elsif(oDataStructure):
    oDataStructure.replace_next_token_with(token.elsif_keyword)
    condition.classify_until(["then"], oDataStructure)
    oDataStructure.replace_next_token_required("then", token.then_keyword)
    sequence_of_statements.detect(oDataStructure, ["elsif", "else", "end"])


@decorators.print_classifier_debug_info(__name__)
def classify_else(oDataStructure):
    oDataStructure.replace_next_token_with(token.else_keyword)
    sequence_of_statements.detect(oDataStructure, ["end"])

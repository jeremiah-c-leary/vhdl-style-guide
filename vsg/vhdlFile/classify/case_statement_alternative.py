# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import case_statement_alternative as token
from vsg.vhdlFile.classify import choices, sequence_of_statements


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    case_statement_alternative ::=
        when choices =>
            sequence_of_statements
    """
    if oDataStructure.is_next_token("when"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("when", token.when_keyword)

    choices.classify_until(["=>"], oDataStructure)

    oDataStructure.replace_next_token_required("=>", token.assignment)

    sequence_of_statements.detect(oDataStructure, ["when", "end"])

# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import record_type_definition as token
from vsg.vhdlFile.classify import element_declaration


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    record_type_definition ::=
        record
            element_declaration
            { element_declaration }
        end record [ *record_type*_simple_name ]
    """

    if oDataStructure.is_next_token("record"):
        classify(oDataStructure)
        return True

    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.record_keyword)

    # TODO:  This while loop could be an issue if end is never found.
    while not oDataStructure.is_next_token("end"):
        element_declaration.classify(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("record", token.end_record_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.record_type_simple_name)

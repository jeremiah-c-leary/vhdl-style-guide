# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import procedure_call as token
from vsg.vhdlFile.classify import actual_parameter_part

lExceptions = ["end", "map", "component", "entity", "configuration", "if"]


@decorators.print_classifier_debug_info(__name__)
@decorators.push_pop_seek_index
def detect(oDataStructure):
    """
    Calling functions:

    concurrent_procedure_call_statement ::=
        [ label : ] [ postponed ] procedure_call ;

    procedure_call_statement ::=
        [ label : ] procedure_call ;

    --------------------------

    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]

    Differentiating a procedure call from anything else is essentially the absence of keywords.
    """

    if oDataStructure.does_string_exist_before_string_honoring_parenthesis_hierarchy("<=", ";"):
        return False

    while not oDataStructure.seek_token_lower_value_is(";"):
        if oDataStructure.get_seek_token_lower_value() in lExceptions:
            return False
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
    return True


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    procedure_call ::=
        *procedure*_name [ ( actual_parameter_part ) ]
    """

    oDataStructure.replace_next_token_with(token.procedure_name)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.open_parenthesis)

        actual_parameter_part.classify(oDataStructure)

        oDataStructure.replace_next_token_required(")", token.close_parenthesis)

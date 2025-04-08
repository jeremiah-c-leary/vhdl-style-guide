# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import physical_type_definition as token
from vsg.vhdlFile.classify import (
    primary_unit_declaration,
    range_constraint,
    secondary_unit_declaration,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    physical_type_definition ::=
        range_constraint
            **units**
                primary_unit_declaration
                { secondary_unit_declaration }
            **end** **units** [ physical_type_simple_name ]
    """
    if oDataStructure.does_string_exist_before_string("units", ";"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    range_constraint.detect(oDataStructure)

    oDataStructure.replace_next_token_required("units", token.units_keyword)

    primary_unit_declaration.detect(oDataStructure)

    while not oDataStructure.is_next_token("end"):
        secondary_unit_declaration.detect(oDataStructure)

    oDataStructure.replace_next_token_with(token.end_keyword)
    oDataStructure.replace_next_token_required("units", token.end_units_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.simple_name)

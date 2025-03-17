# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import physical_type_definition as token
from vsg.vhdlFile import utils
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
    if units_keyword_found_before_semicolon(oDataStructure):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = range_constraint.detect(iToken, lObjects)

    iCurrent = utils.assign_next_token_required("units", token.units_keyword, iToken, lObjects)

    iCurrent = primary_unit_declaration.detect(iCurrent, lObjects)

    while not utils.is_next_token("end", iCurrent, lObjects):
        iCurrent = secondary_unit_declaration.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token(token.end_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required("units", token.end_units_keyword, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_if_not(";", token.simple_name, iCurrent, lObjects)

    return iCurrent


@decorators.print_classifier_debug_info(__name__)
def units_keyword_found_before_semicolon(oDataStructure):
    if oDataStructure.does_string_exist_before_string("units", ";"):
        return True
    return False

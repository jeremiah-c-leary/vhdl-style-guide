# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule,
)


class rule_014(Rule):
    """
    This rule checks the procedure designator exists in the closing of the procedure specification.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       procedure proc is

       end procedure;

    **Fix**

    .. code-block:: vhdl

       procedure proc is

       end procedure proc;
    """

    def __init__(self):
        super().__init__(
            token.subprogram_body.designator,
            token.subprogram_body.semicolon,
            token.procedure_specification.procedure_keyword,
            token.subprogram_body.semicolon,
            token.procedure_specification.designator,
        )
        self.solution = "procedure designator"
        self.groups.append("structure::optional")
        self.filter_tokens = [token.subprogram_declaration.semicolon]

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_procedure_subprogram_body()

        if self._remove_keyword():
            return extract_tokens_for_remove_operation(lToi)
        else:
            return extract_tokens_for_add_operation(lToi)


def extract_tokens_for_remove_operation(lToi):
    lReturn = []

    for oToi in lToi:
        myToi = extract_subprogram_body_end(oToi)

        myToi = myToi.extract_token_and_n_tokens_before_it(token.subprogram_body.designator, 1)
        if myToi is not None:
            lReturn.append(myToi)

    return lReturn


def extract_tokens_for_add_operation(lToi):
    lReturn = []

    for oToi in lToi:
        lReturn.append(extract_subprogram_body_end(oToi))

    return lReturn


def extract_subprogram_body_end(oToi):
    iStart = oToi.get_index_of_last_token_matching(token.subprogram_body.end_keyword)
    iEnd = oToi.get_index_of_last_token_matching(token.subprogram_body.semicolon)
    return oToi.extract_tokens(iStart, iEnd)

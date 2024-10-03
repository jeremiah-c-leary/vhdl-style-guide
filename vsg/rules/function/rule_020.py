# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule,
)


class rule_020(Rule):
    """
    This rule checks the function designator exists in the closing of the function specification.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       function func return integer is

       end function;

    **Fix**

    .. code-block:: vhdl

       function func return integer is

       end function func;
    """

    def __init__(self):
        super().__init__(
            token.subprogram_body.designator,
            token.subprogram_body.semicolon,
            token.function_specification.function_keyword,
            token.subprogram_body.semicolon,
            token.function_specification.designator,
        )
        self.solution = "function designator"
        self.groups.append("structure::optional")
        self.filter_tokens = [token.subprogram_declaration.semicolon]

    def _get_tokens_of_interest(self, oFile):
        if self._remove_keyword():
            lToi = oFile.get_function_subprogram_body()
            lReturn = []
            for oToi in lToi:
                myToi = oToi.extract_token_and_n_tokens_before_it(token.subprogram_body.designator, 1)
                if myToi is not None:
                    lReturn.append(myToi)
            return lReturn
        else:
            return oFile.get_function_subprogram_body()

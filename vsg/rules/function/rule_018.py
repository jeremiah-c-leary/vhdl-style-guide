# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import (
    insert_token_right_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule,
)

oInsertToken = token.subprogram_kind.function_keyword

oAnchorToken = token.subprogram_body.end_keyword

oLeftToken = token.function_specification.function_keyword
oRightToken = token.subprogram_body.semicolon

oValueToken = token.function_specification.function_keyword


class rule_018(Rule):
    """
    This rule checks the function keyword exist in the closing of the function specification.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       function func return integer is

       end func;

    **Fix**

    .. code-block:: vhdl

       function func return integer is

       end function func;
    """

    def __init__(self):
        super().__init__(oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = "function keyword"
        self.groups.append("structure::optional")
        self.filter_tokens.append(token.subprogram_declaration.semicolon)

    def _get_add_tokens_of_interest(self, oFile):
        lToi = oFile.get_function_subprogram_body()
        for oToi in lToi:
            oToken = oToi.get_first_token_matching(oValueToken)
            oToi.set_token_value(oToken.get_value())
        return lToi

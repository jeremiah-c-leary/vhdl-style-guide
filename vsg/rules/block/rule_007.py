# -*- coding: utf-8 -*-

from vsg.rules import (
    insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token,
)
from vsg.token import block_statement as token

oInsertToken = token.end_block_label

oAnchorToken = token.semicolon

oLeftToken = token.end_keyword
oRightToken = token.semicolon

oValueToken = token.block_label


class rule_007(insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token):
    """
    This rule checks the block label exists in the closing of the block statement.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end block;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    """

    def __init__(self):
        super().__init__(oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = "label"
        self.groups.append("structure::optional")

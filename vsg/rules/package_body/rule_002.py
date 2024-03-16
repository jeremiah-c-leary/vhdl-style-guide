# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules import insert_tokens_right_of_token_if_it_does_not_exist_before_token
from vsg.token import package_body as token

lInsertTokens = []
lInsertTokens.append(token.end_package_keyword("package"))
lInsertTokens.append(parser.whitespace(" "))
lInsertTokens.append(token.end_body_keyword("body"))


class rule_002(insert_tokens_right_of_token_if_it_does_not_exist_before_token):
    """
    This rule checks for the optional **package body** keywords on the end package body declaration.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       end FIFO_PKG;

    **Fix**

    .. code-block:: vhdl

       end package body FIFO_PKG;
    """

    def __init__(self):
        super().__init__(lInsertTokens, token.end_keyword, token.semicolon)
        self.solution = "*package body* keywords"
        self.groups.append("structure::optional")

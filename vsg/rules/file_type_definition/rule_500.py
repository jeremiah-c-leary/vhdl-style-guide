# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.file_type_definition.file_keyword)


class rule_500(token_case):
    """
    This rule checks the **file** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       type integer_file is FILE of integer;


    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

       type integer_file is file of integer;

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")

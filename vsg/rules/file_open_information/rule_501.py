# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.file_open_information.file_open_kind_expression)


class rule_501(token_case):
    """
    This rule checks the file open kind expression has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         FILE defaultImage : load_file_type open READ_MODE is load_file_name;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         file defaultImage : load_file_type open read_mode is load_file_name;

       begin
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")

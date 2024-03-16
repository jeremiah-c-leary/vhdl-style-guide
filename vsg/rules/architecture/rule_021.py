# -*- coding: utf-8 -*-

from vsg.rules import token_case
from vsg.token import architecture_body as token


class rule_021(token_case):
    """
    This rule checks the proper case of the **begin** keyword.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
    """

    def __init__(self):
        super().__init__([token.begin_keyword])
        self.groups.append("case::keyword")

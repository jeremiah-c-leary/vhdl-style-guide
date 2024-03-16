# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.loop_statement.end_loop_label)


class rule_504(token_case_with_prefix_suffix):
    """
    This rule checks the proper case of the end label on a loop statement.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         end loop LABEL;
         end loop Label;

    **Fix**

    .. code-block:: vhdl

         end loop label;
         end loop label;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::label")

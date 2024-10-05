# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.bit_string_literal.bit_value_string)


class rule_501(token_case):
    """
    This rule checks the bit value has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    The default style is :code:`upper`.

    **Violation**

    .. code-block:: vhdl

        signal test : my_vector := x"FFF";


    **Fix**

    .. code-block:: vhdl

       signal test : my_vector := x"fff";
    """

    def __init__(self):
        super().__init__(lTokens)
        self.case = "upper"

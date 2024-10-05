# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.bit_string_literal.base_specifier)

# TODO problem is does_not_contain_any_alpha_characters - it drops out if token starts with ".

class rule_500(token_case):
    """
    This rule checks the base specifier has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

        signal test : my_vector := X"FFF";


    **Fix**

    .. code-block:: vhdl

       signal test : my_vector := x"FFF";
    """

    def __init__(self):
        super().__init__(lTokens)

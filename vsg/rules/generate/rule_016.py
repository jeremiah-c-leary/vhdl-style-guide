# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.case_generate_alternative.when_keyword)


class rule_016(token_indent):
    """
    This rule checks the indent of the **when** keyword in generate case statements.

    **Violation**

    .. code-block:: vhdl

       GEN_LABEL : case condition generate
         when 0 =>
           when 1 =>
       when 2 =>

    **Fix**

    .. code-block:: vhdl

       GEN_LABEL : case condition generate
         when 0 =>
         when 1 =>
         when 2 =>
    """

    def __init__(self):
        super().__init__(lTokens)

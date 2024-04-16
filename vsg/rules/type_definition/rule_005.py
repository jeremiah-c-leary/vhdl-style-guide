# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.enumeration_type_definition.enumeration_literal)


class rule_005(token_indent):
    """
    This rule checks the indent of multiline enumerated types.

    **Violation**

    .. code-block:: vhdl

       type state_machine is (
       idle,
         write,
       read,
          done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (
         idle,
         write,
         read,
         done);
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Ensure proper indentation."

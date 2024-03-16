# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import existence_of_tokens_which_should_not_occur

lTokens = []
lTokens.append(token.signal_declaration.assignment_operator)


class rule_007(existence_of_tokens_which_should_not_occur):
    """
    This rule checks for default assignments in signal declarations.

    .. NOTE:: This rule requires the user to remove the default assignments.

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic := '0';

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.solution = "Remove default assignment."
        self.configuration_documentation_link = None

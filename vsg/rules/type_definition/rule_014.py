# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)

lNames = []
lNames.append(token.type_mark.name)


class rule_014(Rule):
    """
    This rule checks for consistent capitalization of type names.

    **Violation**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);

       signal sm : State_Machine;

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);

       signal sm : state_machine;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.bIncludeDeclarativePartNames = True
        self.bIncludeArchitectureBodyDeclarationsInSubprogramBody = True

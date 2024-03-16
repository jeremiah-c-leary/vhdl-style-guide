# -*- coding: utf-8 -*-

from vsg.rules import move_token_next_to_another_token as Rule
from vsg.token import entity_declaration as token


class rule_022(Rule):
    """
    This rule checks the identifier is on the same line as the **entity** keyword.

    **Violation**

    .. code-block:: vhdl

       entity fifo is

       entity
         fifo is

    **Fix**

    .. code-block:: vhdl

       entity fifo is

       entity fifo is
    """

    def __init__(self):
        super().__init__(token.entity_keyword, token.identifier)
        self.subphase = 1
        self.solution = "Move identifier next to *entity* keyword"

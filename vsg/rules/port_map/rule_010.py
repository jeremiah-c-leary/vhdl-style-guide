# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import remove_comments_from_end_of_lines_bounded_by_tokens

oStart = token.component_instantiation_statement.instantiation_label

oEnd = token.component_instantiation_statement.semicolon


class rule_010(remove_comments_from_end_of_lines_bounded_by_tokens):
    """
    This rule checks for comments at the end of the port and generic assignments in instantiations.
    These comments represent additional maintenance.
    They will be out of sync with the entity at some point.
    Refer to the entity for port types, port directions and purpose.

    **Violation**

    .. code-block:: vhdl

       WR_EN => w_wr_en;   -- out : std_logic
       RD_EN => w_rd_en;   -- Reads data when asserted

    **Fix**

    .. code-block:: vhdl

       WR_EN => w_wr_en;
       RD_EN => w_rd_en;
    """

    def __init__(self):
        super().__init__(oStart, oEnd)
        self.solution = "Remove comment."

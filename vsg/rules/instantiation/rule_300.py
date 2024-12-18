# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_300(token_indent):
    """
    This rule checks for the proper indentation of instantiations.

    **Violation**

    .. code-block:: vhdl

       count <= val;
           U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );

    **Fix**

    .. code-block:: vhdl

       count <= val;
       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    """

    def __init__(self):
        super().__init__(lTokens)

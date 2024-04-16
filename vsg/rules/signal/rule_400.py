# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_alignment_between_tokens as Rule

lTokenPairs = []
lTokenPairs.append([token.signal_declaration.signal_keyword, token.signal_declaration.semicolon])


class rule_400(Rule):
    """
    This rule checks alignment of multiline constraints in signal declarations.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal sig_a : my_record(
                element1(7 downto 0),
       element2(3 downto 0)
               );

    **Fix**

    .. code-block:: vhdl

       signal sig_a : my_record(
           element1(7 downto 0),
           element2(3 downto 0)
         );
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.phase = 5
        self.subphase = 3
        self.bIgnoreStartParen = True
        self.bConstraint = True

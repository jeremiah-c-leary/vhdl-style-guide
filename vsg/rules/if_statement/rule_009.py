# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_alignment_between_tokens

lTokenPairs = []
lTokenPairs.append([token.if_statement.if_keyword, token.if_statement.then_keyword])
lTokenPairs.append([token.if_statement.elsif_keyword, token.if_statement.then_keyword])


class rule_009(multiline_alignment_between_tokens):
    """
    This rule checks the alignment of multiline boolean expressions.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       if (a = '0' and b = '1' and
             c = '0') then

    **Fix**

    .. code-block:: vhdl

       if (a = '0' and b = '1' and
           c = '0') then
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.phase = 4
        self.subphase = 2

# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes on signal identifiers.
    Default signal suffix is *_s*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       signal rd_en : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal wr_en_s : std_logic;
       signal rd_en_s : std_logic;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_s"]
        self.solution = "Signal identifiers"

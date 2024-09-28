# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.subtype_declaration.is_keyword, token.type_mark.name])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.std_logic_vector])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.std_ulogic_vector])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.std_ulogic])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.std_logic])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.integer])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.signed])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.unsigned])
lTokens.append([token.subtype_declaration.is_keyword, token.ieee.std_logic_1164.types.natural])


class rule_102(Rule):
    """
    This rule checks for a single space after the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       subtype counter is     unsigned(4 downto 0);

    **Fix**

    .. code-block:: vhdl

       subtype counter is unsigned(4 downto 0);
    """

    def __init__(self):
        super().__init__(lTokens)

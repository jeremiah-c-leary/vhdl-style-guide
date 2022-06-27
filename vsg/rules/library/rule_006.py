
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.use_clause.keyword, token.use_clause.library_name])


class rule_006(Rule):
    '''
    This rule checks for excessive spaces after the **use** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       library ieee;
         use    ieee.std_logic_1164.all;
         use   ieee.std_logic_unsigned.all;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
         use ieee.std_logic_unsigned.all;
    '''
    def __init__(self):
        Rule.__init__(self, 'library', '006', lTokens)

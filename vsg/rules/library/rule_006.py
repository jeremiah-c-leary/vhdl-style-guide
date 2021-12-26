
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.use_clause.keyword, token.use_clause.selected_name])


class rule_006(single_space_between_token_pairs):
    '''
    This rule checks for excessive spaces after the **use** keyword.

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
        single_space_between_token_pairs.__init__(self, 'library', '006', lTokens)
        self.solution = 'Ensure a single space between the *use* keyword and the selected_name.'

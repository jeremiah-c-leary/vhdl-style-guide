
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.library_clause.keyword, token.logical_name_list.logical_name])


class rule_002(single_space_between_token_pairs):
    '''
    This rule checks for excessive spaces after the **library** keyword.

    **Violation**

    .. code-block:: vhdl

       library    ieee;

    **Fix**

    .. code-block:: vhdl

       library ieee;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'library', '002', lTokens)
        self.solution = 'Ensure a single space between the *library* keyword and the logical_name.'

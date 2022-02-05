
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    '''
    This rule checks the signal name has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal WR_EN : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'signal', '004', lTokens)
        self.groups.append('case::name')

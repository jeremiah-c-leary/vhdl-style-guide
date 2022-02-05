
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.identifier)


class rule_008(token_prefix):
    '''
    This rule checks for valid prefixes on signal identifiers.
    Default signal prefix is *s\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       signal rd_en : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal s_wr_en : std_logic;
       signal s_rd_en : std_logic;
    '''

    def __init__(self):
        token_prefix.__init__(self, 'signal', '008', lTokens)
        self.prefixes = ['s_']
        self.solution = 'Signal identifiers'

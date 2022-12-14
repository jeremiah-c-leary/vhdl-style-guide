
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_600(token_prefix):
    '''
    This rule checks for valid prefixes on loop labels.
    The default prefix is *loop\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : for index in 4 to 23 loop

    **Fix**

    .. code-block:: vhdl

       loop_label : for index in 4 to 23 loop
    '''

    def __init__(self):
        token_prefix.__init__(self, 'loop_statement', '600', lTokens)
        self.prefixes = ['loop_']
        self.solution = 'Loop labels'

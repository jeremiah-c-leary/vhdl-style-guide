
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_601(token_suffix):
    '''
    This rule checks for valid suffixes on loop labels.
    The default prefix is *\_loop*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : for index in 4 to 23 loop

    **Fix**

    .. code-block:: vhdl

       label_loop : for index in 4 to 23 loop
    '''

    def __init__(self):
        token_suffix.__init__(self, 'loop_statement', '601', lTokens)
        self.suffixes = ['_loop']
        self.solution = 'Loop labels'

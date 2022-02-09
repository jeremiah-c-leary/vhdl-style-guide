
from vsg import token

from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.component_instantiation_statement.instantiation_label)


class rule_601(token_prefix):
    '''
    This rule checks for valid prefixes on instantiation labels.
    The default prefix is *inst_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       fifo_32x2k : FIFO

    **Fix**

    .. code-block:: vhdl

       inst_fifo_32x2k : FIFO
    '''

    def __init__(self):
        token_prefix.__init__(self, 'instantiation', '601', lTokens)
        self.prefixes = ['inst_']
        self.solution = 'instantiation label'

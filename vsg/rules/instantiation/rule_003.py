
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.component_instantiation_statement.instantiation_label, token.component_instantiation_statement.label_colon])


class rule_003(Rule):
    '''
    This rule checks for a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO: FIFO

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
    '''
    def __init__(self):
        Rule.__init__(self, 'instantiation', '003', lTokens)

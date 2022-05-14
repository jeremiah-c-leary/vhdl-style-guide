
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.component_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.entity_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.configuration_keyword])
lTokens.append([token.component_instantiation_statement.label_colon, token.instantiated_unit.component_name])


class rule_002(Rule):
    '''
    This rule checks for a single space after the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO :FIFO

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
    '''
    def __init__(self):
        Rule.__init__(self, 'instantiation', '002', lTokens)

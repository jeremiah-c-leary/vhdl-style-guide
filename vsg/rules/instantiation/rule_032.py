
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.instantiated_unit.component_keyword, token.instantiated_unit.component_name])


class rule_032(Rule):
    '''
    This rule checks for a single space after the **component** keyword if it is used.

    **Violation**

    .. code-block:: vhdl

       INSTANCE_NAME : component ENTITY_NAME
       INSTANCE_NAME : component   ENTITY_NAME
       INSTANCE_NAME : component  ENTITY_NAME

    **Fix**

    .. code-block:: vhdl

       INSTANCE_NAME : component ENTITY_NAME
       INSTANCE_NAME : component ENTITY_NAME
       INSTANCE_NAME : component ENTITY_NAME
    '''
    def __init__(self):
        Rule.__init__(self, 'instantiation', '032', lTokens)
        self.solution = 'Ensure a single space exists between *component* and the component_name.'

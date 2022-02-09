
from vsg import token

from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens


oInsertToken = token.instantiated_unit.component_keyword('component')

oAnchorToken = token.instantiated_unit.component_name

oStartToken = token.component_instantiation_statement.label_colon

oEndToken = token.component_instantiation_statement.semicolon


class rule_033(insert_token_left_of_token_if_it_does_not_exist_between_tokens):
    '''
    This rule checks for the **component** keyword for a component instantiation.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       INSTANCE_NAME : ENTITY_NAME

    **Fix**

    .. code-block:: vhdl

       INSTANCE_NAME : component ENTITY_NAME
    '''
    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens.__init__(self, 'instantiation', '033', oInsertToken, oAnchorToken, oStartToken, oEndToken)
        self.solution = '*component* keyword'
        self.groups.append('structure::optional')


from vsg import token

from vsg.rules import insert_token_left_of_token_if_it_does_not_exist_between_tokens


oInsertToken = token.instantiated_unit.component_keyword('component')

oAnchorToken = token.instantiated_unit.component_name

oStartToken = token.component_instantiation_statement.label_colon

oEndToken = token.component_instantiation_statement.semicolon


class rule_033(insert_token_left_of_token_if_it_does_not_exist_between_tokens):
    '''
    Removes the optional *component* keyword.
    '''
    def __init__(self):
        insert_token_left_of_token_if_it_does_not_exist_between_tokens.__init__(self, 'instantiation', '033', oInsertToken, oAnchorToken, oStartToken, oEndToken)
        self.solution = '*component* keyword'

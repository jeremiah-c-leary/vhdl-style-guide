
from vsg.rules import move_token_next_to_another_token

from vsg.token import component_declaration as token


class rule_005(move_token_next_to_another_token):
    '''
    Checks the "is" keyword is on the same line as the component keyword.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'component', '005', token.identifier, token.is_keyword)
        self.solution = 'Ensure *is* keyword is on the same line as the entity name.'


from vsg.rules import move_token_next_to_another_token

from vsg.token import architecture_body as token


class rule_006(move_token_next_to_another_token):
    '''
    Architecture rule 006 checks the "is" keyword is on the same line as the entity name.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'architecture', '006', token.entity_name, token.is_keyword)
        self.solution = 'Ensure *is* keyword is on the same line as the entity name.'

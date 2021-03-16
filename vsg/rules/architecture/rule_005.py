

from vsg.rules import move_token_next_to_another_token

from vsg.token import architecture_body as token


class rule_005(move_token_next_to_another_token):
    '''
    Architecture rule 005 checks the "of" keyword is on the same line as the architecture identifier.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'architecture', '005', token.identifier, token.of_keyword)
        self.solution = 'Ensure *of* keyword is on the same line as the architecture identifier.'

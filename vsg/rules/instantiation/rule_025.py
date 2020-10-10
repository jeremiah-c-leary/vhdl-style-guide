
from vsg.rules import move_token_next_to_another_token

from vsg.token import port_map_aspect as token


class rule_025(move_token_next_to_another_token):
    '''
    Checks the **map** keyword is on the same line as the (.
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'instantiation', '025', token.map_keyword, token.open_parenthesis)
        self.solution = 'Move the ( to the same line as the "port map" keyword.'

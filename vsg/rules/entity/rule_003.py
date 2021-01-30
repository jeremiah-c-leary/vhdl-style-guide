
from vsg.rules import previous_line

from vsg.token import entity_declaration as token


class rule_003(previous_line):
    '''
    Checks for a blank line above the "entity" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'entity', '003', [token.entity_keyword])

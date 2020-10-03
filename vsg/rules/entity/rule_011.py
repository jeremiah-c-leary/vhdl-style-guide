
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_011(single_space_between_tokens):
    '''
    Checks for a single space between the entity end keyword and the entityidentifier and is keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '011', token.end_keyword, token.end_entity_keyword)
        self.solution = 'Reduce spaces between *end* keyword and *entity* keyword to a single space.'

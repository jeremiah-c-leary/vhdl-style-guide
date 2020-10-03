
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_013(single_space_between_tokens):
    '''
    Checks for a single space between the entity end keyword and the entityidentifier and is keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '013', token.end_entity_keyword, token.entity_simple_name)
        self.solution = 'Reduce spaces between *entity* keyword and the entity simple name to a single space.'

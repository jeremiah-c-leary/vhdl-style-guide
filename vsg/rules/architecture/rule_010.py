
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist

from vsg.token import architecture_body as token

class rule_010(insert_token_right_of_token_if_it_does_not_exist):
    '''
    Architecture rule 010 checks for "architecture" in the "end architecture statement.
    '''
    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist.__init__(self, 'architecture', '010', token.end_architecture_keyword('architecture'), token.end_keyword)
        self.solution = '*architecture* keyword.'

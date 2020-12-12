
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist

from vsg.token import component_declaration as token


class rule_021(insert_token_right_of_token_if_it_does_not_exist):
    '''
    Component rule 005 checks the "is" keyword is used.
    '''
    def __init__(self):
        insert_token_right_of_token_if_it_does_not_exist.__init__(self, 'component', '021', token.is_keyword('is'), token.identifier)
        self.solution = '*is* keyword.'

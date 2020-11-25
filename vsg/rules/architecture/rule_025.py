
from vsg.rules import is_token_value_one_of

from vsg.token import architecture_body as token


class rule_025(is_token_value_one_of):
    '''
    Architecture rule 025 checks for valid architecture names.
    '''

    def __init__(self):
        is_token_value_one_of.__init__(self, 'architecture', '025', token.identifier)

    def _get_solution(self, iLineNumber):
        return 'Architecture identifier must be from this list: ' + ', '.join(self.names)

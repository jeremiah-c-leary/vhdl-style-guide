
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token


class rule_026(align_tokens_in_region_between_tokens):
    '''
    Architecture rule 025 checks for valid architecture names.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'architecture', '026', [token.file_declaration.colon, token.signal_declaration.colon, token.constant_declaration.colon, token.variable_declaration.colon], token.architecture_body.is_keyword, token.architecture_body.begin_keyword)
        self.solution = 'Align identifer.'

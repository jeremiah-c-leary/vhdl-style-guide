
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.constant_declaration.colon)


class rule_401(align_tokens_in_region_between_tokens):
    '''
    Procedure rule 401 checks the colons are in the same column for all declarations
    in the procedure declarative part.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'procedure', '401', lAlign, token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword)
        self.solution = 'Align :.'
        self.subphase = 2

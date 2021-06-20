
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_kind.function_keyword])
lTokens.append([token.subprogram_body.end_keyword, token.subprogram_body.designator])
lTokens.append([token.subprogram_kind.function_keyword, token.subprogram_body.designator])

class rule_101(single_space_between_token_pairs):
    '''
    Procedure rule 101 checks for a single space between keywords in the closing part of a function specification.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'function', '101', lTokens)
        self.solution = 'Ensure a single space between the keywords in the closing part of a function specification.'


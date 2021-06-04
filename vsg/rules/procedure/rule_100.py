
from vsg.rules import single_space_between_token_pairs

from vsg.token import procedure_specification as token

lTokens = []
lTokens.append([token.procedure_keyword, token.designator])
#lTokens.append([token.designator, token.is_keyword])
lTokens.append([token.designator, token.open_parenthesis])
#lTokens.append([token.close_parenthesis, token.is_keyword])

class rule_100(single_space_between_token_pairs):
    '''
    Procedure rule 100 checks for a single space between keywords in the opening part of a procedure definition.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'procedure', '100', lTokens)
        self.solution = 'Ensure a single space between the keywords in the opening part of a procedure definition.'


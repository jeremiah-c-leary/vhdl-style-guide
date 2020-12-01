
from vsg.rules import remove_tokens

from vsg.token import case_statement as token

lTokens = []
lTokens.append(token.end_case_label)


class rule_020(remove_tokens):
    '''
    Case rule 020 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        remove_tokens.__init__(self, 'case', '020', lTokens)
        self.solution = 'Remove Label'


from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.end_process_label)


class rule_036(token_prefix):
    '''
    Constant rule 036 checks for prefixes in process labels.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'process', '036', lTokens)
        self.prefixes = ['proc_']
        self.solution = 'Process labels'

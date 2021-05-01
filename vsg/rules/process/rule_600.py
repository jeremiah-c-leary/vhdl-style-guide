
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.end_process_label)


class rule_600(token_suffix):
    '''
    Constant rule 600 checks for suffixes in process labels.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'process', '600', lTokens)
        self.suffixes = ['_proc']
        self.solution = 'Process labels'

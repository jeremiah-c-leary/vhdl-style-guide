
from vsg import deprecated_rule


class rule_010(deprecated_rule.Rule):
    '''
    The function of this rule has been moved to rule ieee_500.
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'signal', '010')
        self.message.append('Rule ' + self.unique_id + ' has been replaced with rule ieee_500.')

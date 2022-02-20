
from vsg import deprecated_rule


class rule_027(deprecated_rule.Rule):
    '''
    The function of this rule has been moved to whitespace_200.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'context', '027')
        self.message.append('Rule ' + self.unique_id + ' has been moved to whitespace_200.')

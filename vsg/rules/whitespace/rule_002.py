
from vsg import deprecated_rule


class rule_002(deprecated_rule.Rule):
    '''
    This rule has been deprecated.

    VSG changes tabs to spaces when a file is read in.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'whitespace', '002')
        self.message.append('Rule ' + self.unique_id + ' has been deprecated.')

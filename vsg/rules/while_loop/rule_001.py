
from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    '''
    This rule has been moved to **iteration_scheme_300**.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'while_loop', '001')
        self.message.append('Rule ' + self.unique_id + ' has been moved to iteration_scheme_300.')

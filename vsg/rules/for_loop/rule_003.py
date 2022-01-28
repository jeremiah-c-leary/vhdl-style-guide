
from vsg import deprecated_rule


class rule_003(deprecated_rule.Rule):
    '''
    This rule has been moved to **loop_statement_503**.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'for_loop', '003')
        self.message.append('Rule ' + self.unique_id + ' move been moved to loop_statement_503.')

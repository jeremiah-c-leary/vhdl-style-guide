
from vsg import deprecated_rule


class rule_002(deprecated_rule.Rule):
    '''
    This rule has been moved to **loop_statement_302**.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self)
        self.message.append('Rule ' + self.unique_id + ' has been moved to loop_statement_302.')

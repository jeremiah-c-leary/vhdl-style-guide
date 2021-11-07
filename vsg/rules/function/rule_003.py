
from vsg import deprecated_rule


class rule_003(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'function', '003')
        self.message.append('Rule ' + self.unique_id + ' has been merged into function_100.')

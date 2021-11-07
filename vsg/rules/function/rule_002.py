
from vsg import deprecated_rule


class rule_002(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'function', '002')
        self.message.append('Rule ' + self.unique_id + ' has been merged into function_100.')

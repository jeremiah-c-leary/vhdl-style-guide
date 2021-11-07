
from vsg import deprecated_rule


class rule_018(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '018')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_006.')

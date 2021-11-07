
from vsg import deprecated_rule


class rule_030(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '030')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to generic_map_007.')

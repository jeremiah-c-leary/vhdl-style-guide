
from vsg import deprecated_rule


class rule_024(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '024')
        self.message.append('Rule ' + self.unique_id + ' has been split into rules:')
        self.message.append('  generic_map_008')
        self.message.append('  rule port_map_005')

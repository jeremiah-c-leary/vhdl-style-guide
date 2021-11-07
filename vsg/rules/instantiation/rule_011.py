
from vsg import deprecated_rule


class rule_011(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '011')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to port_map_002.')

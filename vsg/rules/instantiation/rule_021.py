
from vsg import deprecated_rule


class rule_021(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '021')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule port_map_009.')


from vsg import deprecated_rule


class rule_023(deprecated_rule.Rule):
    '''
    This rule has been renamed to `port_map_010 <port_map_rules.html#port-map-010>`_.
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self)
        self.message.append('Rule ' + self.unique_id + ' has been renamed to port_map_010.')

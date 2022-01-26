
from vsg import deprecated_rule


class rule_007(deprecated_rule.Rule):
    '''
    This rule has been renamed to `port_map_004 <port_map_rules.html#port-map-004>`_.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '007')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to port_map_004.')

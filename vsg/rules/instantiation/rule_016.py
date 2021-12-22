
from vsg import deprecated_rule


class rule_016(deprecated_rule.Rule):
    '''
    This rule has been renamed to `generic_map_002 <generic_map_rules.html#generic-map-002>`_.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '016')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_002.')

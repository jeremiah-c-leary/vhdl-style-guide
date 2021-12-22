
from vsg import deprecated_rule


class rule_017(deprecated_rule.Rule):
    '''
    This rule has been renamed to `generic_map_005 <generic_map_rules.html#generic-map-005>`_.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '017')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_005.')

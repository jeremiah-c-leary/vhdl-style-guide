
from vsg import deprecated_rule


class rule_013(deprecated_rule.Rule):
    '''
    Constant rule 601 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'instantiation', '013')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_001.')

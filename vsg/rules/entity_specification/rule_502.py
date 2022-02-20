
from vsg import deprecated_rule


class rule_502(deprecated_rule.Rule):
    '''
    This rule has been deprecated.  The case of *entity_designator* should be enforced by other rules.
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'entity_specification', '502')
        self.message.append('Rule ' + self.unique_id + ' has been deprecated.')

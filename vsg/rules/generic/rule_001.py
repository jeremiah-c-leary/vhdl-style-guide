
from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    '''
    This rule has been moved to `entity_200 <entity_rules.html#entity-200>`_ to isolate the rule to entity declarations.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'generic', '001')
        self.message.append('Rule ' + self.unique_id + ' has been moved to entity_200.')

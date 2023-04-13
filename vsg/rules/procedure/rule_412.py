
from vsg.deprecated_rule import Rule


class rule_412(Rule):
    '''
    This rule has been superceeded by rule `architecture_027 <architecture_rules.html#architecture-027>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'procedure', '412')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by rule architecture_027.')

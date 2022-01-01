
from vsg.deprecated_rule import Rule


class rule_005(Rule):
    '''
    This rule has been deprecated and replaced with rule `process_400 <process_rules.html#process-400>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'sequential', '005')
        self.message.append('Rule ' + self.unique_id + ' has been merged into process_400.')
